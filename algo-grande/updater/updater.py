"""
Actualizador automático — tabla de despidos por AI
Corre al encender la máquina, máximo una vez al día.
Busca noticias en RSS, analiza con Claude, actualiza la tabla en index.html y hace push a GitHub.
"""

import json
import os
import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path

import feedparser
import anthropic

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR     = Path(__file__).parent.parent   # algo-grande/
UPDATER_DIR  = Path(__file__).parent          # algo-grande/updater/
LAYOFFS_JSON = UPDATER_DIR / "layoffs.json"
INDEX_HTML   = BASE_DIR / "index.html"
LAST_RUN     = UPDATER_DIR / ".last_run"

# ── Fuentes RSS ────────────────────────────────────────────────────────────────
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.a.dj.com/rss/RSSWSJD.xml",
    "https://www.reuters.com/technology/rss",
]

KEYWORDS = [
    "layoff", "lay off", "job cut", "fired", "replaced with ai",
    "ai replaces", "automation cut", "workforce reduction", "despido",
]

# ── Control de frecuencia ──────────────────────────────────────────────────────
def ya_corrio_hoy():
    if not LAST_RUN.exists():
        return False
    ultimo = datetime.fromisoformat(LAST_RUN.read_text().strip())
    return datetime.now() - ultimo < timedelta(hours=20)

def marcar_ejecutado():
    LAST_RUN.write_text(datetime.now().isoformat())

# ── Data ───────────────────────────────────────────────────────────────────────
def cargar_despidos():
    if LAYOFFS_JSON.exists():
        return json.loads(LAYOFFS_JSON.read_text(encoding="utf-8"))
    return {"despidos": [], "ultima_actualizacion": None}

def guardar_despidos(data):
    data["ultima_actualizacion"] = datetime.now().strftime("%Y-%m-%d")
    LAYOFFS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

# ── RSS ────────────────────────────────────────────────────────────────────────
def obtener_articulos():
    articulos = []
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:25]:
                titulo  = entry.get("title", "")
                resumen = entry.get("summary", "")
                texto   = f"{titulo} {resumen}".lower()
                if any(k in texto for k in KEYWORDS):
                    articulos.append({
                        "titulo":  titulo,
                        "resumen": resumen[:600],
                        "fecha":   entry.get("published", "")[:10],
                    })
        except Exception as e:
            print(f"  ⚠ Error leyendo {url}: {e}")
    return articulos

# ── Claude ─────────────────────────────────────────────────────────────────────
def analizar_con_claude(articulos, despidos_existentes):
    if not articulos:
        return []

    client = anthropic.Anthropic()
    empresas_existentes = [d["empresa"].lower() for d in despidos_existentes]

    prompt = f"""Analiza estos artículos sobre despidos y automatización con AI.

Para cada caso relevante extrae:
- empresa: nombre exacto
- industria: sector en español (Tecnología, Fintech, Logística, Salud, Banca, Educación, E-commerce, Telecomunicaciones, Medios, Manufactura, etc.)
- empleos: número entero (sin texto, solo el número)
- ai_explicito: true si AI fue citado como razón directa, false si fue factor
- año: año del despido (número entero)

Reglas:
- Solo incluir casos con número concreto de empleos afectados (mínimo 100)
- NO incluir empresas ya en esta lista: {empresas_existentes}
- Si un artículo no tiene datos concretos, ignorarlo

Responde ÚNICAMENTE con un array JSON válido. Si no hay casos nuevos: []

Artículos:
{json.dumps(articulos, ensure_ascii=False)}"""

    try:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}]
        )
        texto = msg.content[0].text.strip()
        match = re.search(r'\[.*\]', texto, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"  ⚠ Error con Claude: {e}")
    return []

# ── HTML ───────────────────────────────────────────────────────────────────────
def generar_tabla_html(despidos):
    ordenados = sorted(despidos, key=lambda x: x.get("empleos", 0), reverse=True)
    total     = sum(d.get("empleos", 0) for d in ordenados)
    fecha     = datetime.now().strftime("%d/%m/%Y")

    filas = ""
    for d in ordenados:
        marca       = " ✦" if d.get("ai_explicito") else ""
        empleos_fmt = f"{d['empleos']:,}".replace(",", ".")
        filas += f"""            <tr style="border-bottom:1px solid var(--cream);">
              <td style="padding:0.6rem; font-weight:500; color:var(--ink);">{d['empresa']}</td>
              <td style="padding:0.6rem; color:var(--gray);">{d['industria']}</td>
              <td style="padding:0.6rem; text-align:right; color:var(--gray);">{empleos_fmt}{marca}</td>
            </tr>\n"""

    total_fmt = f"+{total:,}".replace(",", ".")

    return f"""      <p class="fade-in">Esto no es proyección. Ya está pasando:</p>

      <div class="fade-in" style="overflow-x:auto; margin:1.2rem 0;">
        <table style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="border-bottom:2px solid var(--ink);">
              <th style="text-align:left; padding:0.5rem 0.6rem; font-size:0.68rem; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; color:var(--light);">Empresa</th>
              <th style="text-align:left; padding:0.5rem 0.6rem; font-size:0.68rem; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; color:var(--light);">Industria</th>
              <th style="text-align:right; padding:0.5rem 0.6rem; font-size:0.68rem; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; color:var(--light);">Empleos</th>
            </tr>
          </thead>
          <tbody>
{filas}            <tr style="border-bottom:2px solid var(--ink);"></tr>
            <tr style="background:var(--cream);">
              <td colspan="2" style="padding:0.6rem; font-weight:500; color:var(--ink);">Total documentado</td>
              <td style="padding:0.6rem; text-align:right; font-weight:500; color:var(--red);">{total_fmt}</td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:0.72rem; color:var(--light); margin-top:0.6rem;">✦ AI citado explícitamente como razón principal · Los demás: reestructuración donde AI fue factor · Actualizado: {fecha}</p>
      </div>"""

def actualizar_html(tabla_html):
    contenido = INDEX_HTML.read_text(encoding="utf-8")
    inicio = "<!-- TABLA_DESPIDOS_INICIO -->"
    fin    = "<!-- TABLA_DESPIDOS_FIN -->"
    nuevo  = f"{inicio}\n{tabla_html}\n      {fin}"
    contenido = re.sub(
        rf"{re.escape(inicio)}.*?{re.escape(fin)}",
        nuevo,
        contenido,
        flags=re.DOTALL
    )
    INDEX_HTML.write_text(contenido, encoding="utf-8")

# ── Git ────────────────────────────────────────────────────────────────────────
def push_a_github():
    try:
        subprocess.run(
            ["git", "add", "updater/layoffs.json", "index.html"],
            cwd=BASE_DIR, check=True, capture_output=True
        )
        fecha = datetime.now().strftime("%Y-%m-%d")
        resultado = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=BASE_DIR
        )
        if resultado.returncode != 0:  # hay cambios
            subprocess.run(
                ["git", "commit", "-m", f"Actualiza tabla despidos AI — {fecha}"],
                cwd=BASE_DIR, check=True, capture_output=True
            )
            subprocess.run(
                ["git", "push"],
                cwd=BASE_DIR, check=True, capture_output=True
            )
            print("  ✅ Push a GitHub exitoso")
        else:
            print("  ℹ Sin cambios nuevos para publicar")
    except subprocess.CalledProcessError as e:
        print(f"  ⚠ Error en git: {e}")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print(f"\n{'='*50}")
    print(f"  Updater algo-grande — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*50}")

    if ya_corrio_hoy():
        print("  Ya corrió hoy. Hasta mañana.")
        return

    data = cargar_despidos()
    print(f"  {len(data['despidos'])} empresas en base de datos actual")

    print("  🔍 Buscando noticias...")
    articulos = obtener_articulos()
    print(f"  {len(articulos)} artículos relevantes encontrados")

    if articulos:
        print("  🤖 Analizando con Claude...")
        nuevos = analizar_con_claude(articulos, data["despidos"])
        if nuevos:
            print(f"  ✅ {len(nuevos)} nuevas empresas: {[n['empresa'] for n in nuevos]}")
            data["despidos"].extend(nuevos)
            guardar_despidos(data)
        else:
            print("  Sin novedades hoy")

    print("  📝 Actualizando tabla en index.html...")
    tabla = generar_tabla_html(data["despidos"])
    actualizar_html(tabla)

    print("  📤 Publicando en GitHub Pages...")
    push_a_github()

    marcar_ejecutado()
    print("  ✅ Listo\n")

if __name__ == "__main__":
    main()

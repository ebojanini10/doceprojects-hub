# DoceProjects — Automatización e IA para empresas colombianas

**Repo:** `mclara-martinez/doceprojects` (private)
**Equipo:** Emiliano Bojanini + María Clara Martínez + David Posada + Santiago Restrepo

---

## Qué es DoceProjects

Consultora de automatización e inteligencia artificial. El modelo opera bajo el concepto **12:12** — velocidad, precisión y urgencia como diferenciadores.

**Regla de oro:** El cliente no nos puede necesitar. Todo sistema debe perdurar sin nosotros.

---

## Archivos clave

| Archivo | Propósito |
|---------|-----------|
| `brand-manual.html` / `.pdf` | Brand book visual DoceProjects |
| `business-playbook.md` | Metodología completa: Discovery, propuesta, 12:12 |
| `proposal-template.html` | Template HTML para propuestas comerciales |
| `proposal-demo.html` | Demo de propuesta con datos ficticios |
| `dashboard.html` | Dashboard interno de proyectos activos |
| `projects.json` | Estado de todos los proyectos (fuente de verdad) |
| `team.json` | Bios y roles del equipo |

---

## Flujo comercial

```
WhatsApp (agente AI) → Diagnóstico tech stack
→ NDA (firmamos primero)
→ Discovery Call (grabado, sin límite de tiempo)
→ Propuesta HTML enviada al siguiente 12:12
→ 12 horas para aceptar al precio original
→ Implementación → Mantenimiento
```

---

## Regla de deployment de propuestas (OBLIGATORIO)

**Toda propuesta comercial DEBE deployarse en el hub centralizado. Sin excepción.**

| Paso | Comando / Acción |
|------|------------------|
| 1. Crear HTML | Usar `proposal-template.html` como base |
| 2. Deploy | `cd mclaramartinez.github.io && ./deploy.sh <slug> <propuesta.html>` |
| 3. URL | `https://prop.doceprojects.com/<slug>/` |
| 4. Password | `doce-<slug>` (default, personalizable como 3er arg) |
| 5. projects.json | Agregar campo `proposal: { url, password, slug }` al proyecto |
| 6. Dashboard | Verificar que el link y password aparecen en la card |

**Aplica para todo el equipo:** Clara, Emiliano, David, Santiago.
**El dashboard es la fuente de verdad** — si no tiene el link y el password, no está deployada.

---

## Equipo

| Persona | Rol |
|---------|-----|
| **Emiliano Bojanini** | Founder — Discovery, servicio al cliente, entendimiento de negocios |
| **María Clara Martínez** | Co-Founder — Ejecución, herramientas, documentación, operaciones |
| **David Posada** | Implementation Specialist — Onboarding en sitio, videollamadas |
| **Santiago Restrepo** | Security & Infrastructure — Seguridad código, mantenibilidad |

---

## Proyectos activos (ver projects.json para detalle)

| Cliente | Stage | Repo(s) |
|---------|-------|---------|
| Sky Flowers | Implementación | `ebojanini10/skyflowers-platform`, `skyflowers-poscosecha-planner` |
| Loretta Puro Antojo | Discovery | `ebojanini10/loretta-cliente-bogota` |
| Obras y Montajes | Propuesta | `ebojanini10/obras-montajes-sistema` |
| EQR Roses | Discovery | `ebojanini10/eqr-roses-sistema`, `eqr-roses-client` |
| Construhigiénicas | Propuesta | `mclara-martinez/construhigienicas` |
| Casa Ardente | Discovery | `ebojanini10/casa-ardente-sistema`, `casa-ardente-propuesta` |
| Paulina Arquitectura | Implementación | `ebojanini10/arquitectura-bot` |
| Hortensia Vision | Implementación | `ebojanini10/skyflowers-hortensia-vision` |
| Álamo SAS | Lead | `ebojanini10/alamo-sistema` |
| Origami | Lead | `ebojanini10/origami-sistema` |
| Flashy | Lead | `ebojanini10/flashy-sistema` |
| Terramística / This Is | Implementación | `ebojanini10/terramistica-metaads`, `this-is-entregables` |
| Actaia (ReunIA) | Implementación | `ebojanini10/actaia` |
| Mattilda | Propuesta | `ebojanini10/mattilda-sistema` |
| Glow Institute | Discovery | `ebojanini10/estetica-santiago-manuela` |

---

## Pendientes internos

- [ ] Discovery Call guide (ruta crítica + preguntas guía)
- [ ] Contrato de servicios template
- [ ] Workflow automático de aceptación de propuesta
- [x] Configurar dominio custom (GitHub Pages) — prop/props/ops.doceprojects.com
- [ ] Unit Economics por tipo de proyecto

## Hub de propuestas (prop.doceprojects.com)

Repo: `mclara-martinez/mclaramartinez.github.io` (PUBLIC)
Todas las propuestas se despliegan aquí como `/<client>/index.html`, encriptadas con StatiCrypt.
Deploy: `./deploy.sh <client-slug> <source.html> [password]` — password default: `doce-<slug>`

### Propuestas deployadas

| Cliente | URL | Password |
|---------|-----|----------|
| Construhigiénicas | `prop.doceprojects.com/construhigienicas/` | `doce-construhigienicas` |
| Casa Ardente | `prop.doceprojects.com/casa-ardente/` | `doce-casa-ardente` |
| EQR Roses | `prop.doceprojects.com/eqr/` | `doce-eqr` |
| Demo | `prop.doceprojects.com/demo/` | `doce-demo` |

### Completado

- [x] Construhigiénicas deployada
- [x] Crear deploy.sh (script de despliegue)
- [x] Agregar ebojanini10 como colaborador (invitación enviada, pendiente aceptar)
- [x] Migrar casa-ardente (redirect desde URL vieja `/casa-ardente-propuesta/`)
- [x] Migrar EQR
- [x] Migrar demo
- [x] Estandarizar StatiCrypt — todas usan salt compartido de `.staticrypt.json`
- [x] 404.html con redirect automático props → prop (JS fallback)

### Pendiente — requiere GoDaddy DNS (cuenta Emiliano)

- [ ] Fix eqr.doceprojects.com — cambiar A records (AWS) a CNAME → `mclaramartinez.github.io`
- [ ] Redirect props → prop — cambiar CNAME de `ebjoanini10.github.io` (typo) a `mclaramartinez.github.io`, o eliminar

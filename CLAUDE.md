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
| Álamo SAS | Discovery | `ebojanini10/alamo-sistema` |
| Origami | Discovery | `ebojanini10/origami-sistema` |
| Flashy | Discovery | `ebojanini10/flashy-sistema` |
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

- [x] Construhigiénicas deployada (password: `doce-construhigienicas`)
- [ ] Crear deploy.sh (script de despliegue)
- [ ] Agregar ebojanini10 como colaborador
- [ ] Migrar casa-ardente (mantener URL vieja)
- [ ] Migrar EQR (esperar confirmación cliente)
- [ ] Migrar demo
- [ ] Fix eqr.doceprojects.com (DNS roto, 405)
- [ ] Redirect props → prop (después de migrar todo)
- [ ] Estandarizar StatiCrypt para todas las propuestas

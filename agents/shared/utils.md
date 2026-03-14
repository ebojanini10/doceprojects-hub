# Shared Utilities — DoceProjects Agent System

Reference documentation for all agents. Defines data contracts, logging, notifications, and conventions.

---

## 1. projects.json — Source of Truth

**Location:** `/projects.json` (repo root)

Every agent reads and writes to this single file. There is no other canonical source for project state.

### Reading

```
Use the Read tool to read /projects.json at the start of every operation.
Never cache projects.json across invocations — always read fresh.
```

### Writing

```
Use the Edit tool to modify /projects.json.
Only change the specific fields you need — do not rewrite the entire file.
After writing, update the top-level "lastUpdated" field to the current ISO timestamp.
```

### Schema Reference

```json
{
  "version": 2,
  "lastUpdated": "2026-03-09T12:00:00.000Z",
  "stages": [
    {
      "id": "lead|discovery|propuesta|implementacion|mantenimiento|interno",
      "label": "Human-readable label",
      "color": "#hex",
      "order": 0
    }
  ],
  "projects": [
    {
      "id": "slug-kebab-case",
      "name": "Display Name",
      "repos": ["owner/repo-name"],
      "stage": "stage-id",
      "proposal": {
        "url": "https://prop.doceprojects.com/<slug>/",
        "password": "doce-<slug>",
        "slug": "<slug>"
      },
      "tasks": [
        {
          "id": "t-xx-n",
          "text": "Task description",
          "done": false,
          "priority": "HIGH|MEDIUM|LOW",
          "assignee": "Name"
        }
      ],
      "notes": "Free-text notes",
      "createdAt": "2026-01-15T00:00:00.000Z"
    }
  ],
  "actionItems": [
    {
      "id": "a1",
      "text": "Action item description",
      "done": false,
      "priority": "HIGH|MEDIUM|LOW",
      "assignee": "Name",
      "category": "operacion|legal|tech|negocio|producto|infra"
    }
  ]
}
```

### Stage IDs and Progression

| Order | ID               | Label            | Color   |
|-------|------------------|------------------|---------|
| 0     | `lead`           | Lead             | #9CA3AF |
| 1     | `discovery`      | Discovery        | #F59E0B |
| 2     | `propuesta`      | Propuesta        | #3B82F6 |
| 3     | `implementacion` | Implementacion   | #8B5CF6 |
| 4     | `mantenimiento`  | Mantenimiento    | #16A34A |
| 5     | `interno`        | Interno          | #6B7280 |

Valid forward transitions: `lead -> discovery -> propuesta -> implementacion -> mantenimiento`. The `interno` stage is for internal DoceProjects projects and does not follow the standard progression.

### Task ID Convention

Task IDs follow the pattern `t-XX-N` where:
- `XX` = first two letters of the project id (e.g., `sk` for sky-flowers)
- `N` = sequential number within that project

When adding a task, read existing tasks to determine the next sequential number.

### Proposal Object

The `proposal` field is only present for projects that have a deployed proposal. A project in stage `propuesta` WITHOUT a `proposal` object is a blocker that agents must flag.

---

## 2. Event Log

**Location:** `/agents/event-log.jsonl` (repo root, under agents/)

Append-only log of all agent actions. Every agent MUST log its actions here.

### Format (JSON Lines)

Each line is a single JSON object:

```jsonl
{"timestamp":"2026-03-09T12:00:00-05:00","agent":"pm","action":"daily-briefing-generated","project":null,"data":{"projectCount":16,"alertCount":3}}
{"timestamp":"2026-03-09T12:05:00-05:00","agent":"pm","action":"task-added","project":"sky-flowers","data":{"taskId":"t-sk-12","text":"Revisar integracion API","priority":"HIGH","assignee":"Clara"}}
{"timestamp":"2026-03-09T14:30:00-05:00","agent":"propuesta","action":"proposal-deployed","project":"mattilda","data":{"url":"https://prop.doceprojects.com/mattilda/","password":"doce-mattilda"}}
```

### Fields

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `timestamp` | string   | yes      | ISO 8601 with Colombia timezone offset (-05:00) |
| `agent`     | string   | yes      | One of: `pm`, `propuesta`, `qa`, `discovery`, `soporte`, `onboarding`, `finance` |
| `action`    | string   | yes      | Kebab-case description of what happened |
| `project`   | string   | no       | Project ID (null for non-project-specific actions) |
| `data`      | object   | yes      | Arbitrary payload with action-specific details |

### Writing to the Event Log

Use the Bash tool to append a line:

```bash
echo '{"timestamp":"2026-03-09T12:00:00-05:00","agent":"pm","action":"task-added","project":"sky-flowers","data":{"taskId":"t-sk-12"}}' >> /path/to/repo/agents/event-log.jsonl
```

Never overwrite or edit existing lines. This is an append-only log.

### Common Actions by Agent

| Agent       | Actions |
|-------------|---------|
| `pm`        | `daily-briefing-generated`, `task-added`, `task-completed`, `stage-advanced`, `blocker-detected` |
| `propuesta` | `proposal-drafted`, `proposal-deployed`, `proposal-updated` |
| `qa`        | `review-started`, `review-completed`, `issue-found` |
| `discovery` | `call-scheduled`, `call-completed`, `notes-processed` |
| `soporte`   | `ticket-received`, `ticket-resolved`, `escalation-created` |
| `onboarding`| `onboarding-started`, `onboarding-completed`, `training-scheduled` |
| `finance`   | `invoice-generated`, `payment-received`, `payment-overdue` |

---

## 3. WhatsApp Notification Format

All agents use this standardized format when composing WhatsApp messages.

### Template

```
[EMOJI] [AGENT NAME] — DoceProjects
━━━━━━━━━━━━━━━━━
[Message body]
━━━━━━━━━━━━━━━━━
[CLOCK EMOJI] [timestamp in Colombia time]
```

### Agent Identifiers

| Agent       | Emoji | Header |
|-------------|-------|--------|
| PM          | :purple_circle:    | PM AGENT |
| Propuesta   | :blue_circle:    | PROPUESTA AGENT |
| QA          | :green_circle:    | QA AGENT |
| Discovery   | :yellow_circle:    | DISCOVERY AGENT |
| Soporte     | :red_circle:    | SOPORTE AGENT |
| Onboarding  | :white_circle:    | ONBOARDING AGENT |
| Finance     | :orange_circle:    | FINANCE AGENT |

### Example

```
:purple_circle: PM AGENT — DoceProjects
━━━━━━━━━━━━━━━━━
Proyecto Sky Flowers avanzado a etapa Implementacion.
3 tareas HIGH pendientes.
━━━━━━━━━━━━━━━━━
:clock: 2026-03-09 12:00 COT
```

### Rules

- Keep messages concise (WhatsApp truncates long previews)
- Use bullet points for lists
- Include project name in body when relevant
- Timestamps always in Colombia time (COT, UTC-5)

---

## 4. Conventions

### Language

- **Client-facing communications** (WhatsApp messages, proposals, notes visible to clients): Spanish
- **Internal code, comments, variable names, log actions, documentation**: English
- **projects.json field names**: English
- **projects.json content** (task text, notes, project names): Spanish when describing client work

### Timezone

All timestamps use Colombia time (UTC-5, COT). Format ISO 8601 with offset:

```
2026-03-09T12:00:00-05:00
```

### File Paths

All file paths in agent documentation and code are relative to the repo root (`/Users/mclaramartinez/Claude_Code/doceprojects/`), unless specified as absolute.

Key paths:
- `projects.json` — project state
- `agents/event-log.jsonl` — action log
- `agents/shared/utils.md` — this file
- `agents/<agent-name>/SKILL.md` — individual agent skill definition
- `dashboard.html` — internal project dashboard
- `proposal-template.html` — base template for proposals

### Data Integrity Rules

1. **Never delete tasks** — mark as `"done": true` instead
2. **Never delete projects** — move to an appropriate stage or add a note
3. **Never overwrite event-log.jsonl** — append only
4. **Always update `lastUpdated`** when modifying projects.json
5. **Always log to event-log.jsonl** when performing any write action
6. **Read projects.json fresh** at the start of every operation — never rely on cached state

### Team Members (valid assignee values)

| Name      | Full Name              | Role |
|-----------|------------------------|------|
| Clara     | Maria Clara Martinez   | Co-Founder, Ops |
| Emiliano  | Emiliano Bojanini      | Founder, Discovery |
| David     | David Posada           | Implementation |
| Santiago  | Santiago Restrepo      | Security & Infra |

---

## 5. Stack de Herramientas IA — DoceProjects

DoceProjects tiene acceso activo a las siguientes herramientas de IA. **Todos los agentes deben conocer este stack** para identificar oportunidades, estimar costos y generar propuestas precisas.

### Herramientas activas (ya pagadas, $0 adicional por uso)

| Herramienta | Plan | Capacidad mensual | Uso principal |
|---|---|---|---|
| **Claude Max** (Anthropic) | Max $200/mes | Conversaciones y proyectos ilimitados | Guiones, propuestas, código, análisis |
| **ChatGPT Plus** (OpenAI) | Plus $20/mes | Sora 2: ~50 videos hasta 20 seg (priority) + ilimitados en cola | Video hero shots y escenas emocionales |
| **Gemini Advanced** (Google) | Advanced $20/mes | Veo 3.1: ~5-10 videos/día · Más: $0.15/seg | Video con audio nativo, demos de producto |
| **ElevenLabs Creator** | Creator $22/mes | 30 voces clonadas · 30.000 caracteres → ~20 narraciones/mes | Narración y clonación de voz |
| **Grok** (xAI) | Premium ~$16/mes | Chat + búsqueda web en tiempo real · ~150 imágenes/mes | Investigación, tendencias, imágenes Aurora |
| **Gamma Pro** | Pro ~$20/mes | Presentaciones IA ilimitadas | Decks, docs, landing pages |

### Herramientas de video — Generador de Contenido IA

| Herramienta | Plan | Capacidad mensual | Uso en pipeline |
|---|---|---|---|
| **Kling 3.0** | Standard $6.99/mes | 660 créditos → ~16 comerciales/mes | B-roll: hook (0-5s) y social proof (40-55s) |
| **HeyGen 4** | Creator $29/mes | 5 min → 20 escenas de portavoz/mes | Lip-sync portavoz con voz clonada |
| **Midjourney** | Basic $10/mes | ~200 imágenes | Generación de personajes de marca IA |

**Nota Veo 3.1:** Es el único modelo con audio nativo real (diálogo + ambiente en una sola generación). Pay-as-you-go: ~$3 por escena de demo de 20 seg.

### Capacidad de producción de video

Con el stack completo, DoceProjects puede producir:
- **~16 comerciales de 60 seg por mes** (limitante: créditos Kling)
- **Costo real por comercial:** ~$5-6 USD (~$20.000 COP)
- **Tiempo de producción:** 3-4 horas por comercial
- **Formatos de entrega:** 16:9 (YouTube/LinkedIn) + 9:16 (TikTok/Instagram/Reels)
- **100% IA:** voz clonada (ElevenLabs) + personaje generado (Midjourney/Kling) + portavoz lip-sync (HeyGen)

### Stack de desarrollo — lo que DoceProjects construye con

Todo sistema que DoceProjects implementa está construido con este stack. Los agentes deben usarlo como referencia al estimar esfuerzo, revisar propuestas técnicas o hacer onboarding.

| Capa | Tecnología | Uso |
|---|---|---|
| **Lenguaje** | Python 3.11+ | Todo — bots, automatizaciones, scripts, APIs |
| **Framework web** | Flask | Todos los bots y servicios expuestos (un puerto por módulo) |
| **IA / LLM** | Anthropic SDK (`anthropic`) | Claude en todos los agentes y bots |
| **Voz** | ElevenLabs API (`requests`) | Narración y clonación de voz |
| **Transcripción** | OpenAI Whisper | Audio → texto (voz a texto en bots) |
| **WhatsApp** | Meta WhatsApp Business API | Canal principal de todos los bots |
| **PDF** | ReportLab / FPDF2 | Generación de reportes, manuales, actas, disponibles |
| **Excel / Sheets** | `openpyxl`, `pandas` | Exportación de datos, conciliación bancaria |
| **Base de datos cliente** | SQL Server (`pyodbc` + ODBC Driver 17) | Conexión a ERPs como World Office |
| **Data warehouse** | Google BigQuery (`google-cloud-bigquery`) | Analytics y dashboards ejecutivos |
| **Email** | Gmail API (`google-auth`, `googleapiclient`) | Automatización de correos |
| **ERP externo** | Komet API | Integración pedidos flores (Sky Flowers, EQR) |
| **Visión por computadora** | OpenCV + YOLO8 + PyTorch | Detección de enfermedades en plantas (Hortensia Vision) |
| **Scheduler** | Windows Task Scheduler / cron | Tareas programadas (briefing matutino, monitor IT) |
| **Servidor** | Mac Mini `192.168.1.215` + ngrok | Servidor siempre encendido con webhook fijo |
| **Control de versiones** | GitHub (`ebojanini10`) | Todos los repos, privados |

**Convención de puertos:** cada módulo corre en un puerto fijo (5000-5030). Un proceso = un puerto = un `bot_*.py` o `app.py`.

**Lo que NO usamos:** n8n (descartado — Python es más controlable), bases de datos propias (usamos las del cliente), infraestructura cloud propia (todo corre en Mac Mini del cliente o servidor local).

### Implicaciones para cada agente

| Agente | Qué debe saber |
|---|---|
| **Discovery** | Preguntar si el cliente tiene contenido de video. Si no tiene o es malo → oportunidad de Generador de Contenido |
| **Propuesta** | Incluir Generador de Contenido como cluster cuando el cliente tiene producto visual o redes. Ver reglas en `/agents/propuesta/SKILL.md` |
| **Finance** | Costo de producción: ~$5-6 USD/video. Precio mínimo: $800.000 COP. Margen >97% |
| **Tech Review** | El stack es 100% externo (APIs). No requiere infraestructura propia del cliente |
| **Onboarding** | Para activar Generador de Contenido: solicitar al cliente 3 min de audio para clonar voz + foto para personaje |
| **QA** | Verificar entrega de archivos: `script_completo.md` + `prompts_video.json` + `narration.mp3` por comercial |

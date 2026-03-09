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

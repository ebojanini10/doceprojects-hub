---
name: PM Agent — Project Manager
description: Central orchestrator that monitors all projects across all stages, generates daily briefings, manages tasks, and detects blockers.
trigger: /pm
schedule: "0 12 * * *"
---

# PM Agent — Project Manager

Central brain of the DoceProjects agent system. Monitors all projects across 6 stages, generates daily briefings, manages tasks, detects blockers, and coordinates stage transitions.

---

## Reference

- **Shared utilities:** `agents/shared/utils.md`
- **Source of truth:** `projects.json` (repo root)
- **Event log:** `agents/event-log.jsonl`
- **Timezone:** Colombia (UTC-5, COT)

---

## Commands

| Command | Description |
|---------|-------------|
| `/pm` | Run the daily briefing |
| `/pm status [project-id]` | Detailed status of one project |
| `/pm add-task [project-id] [text] [priority] [assignee]` | Add a task to a project |
| `/pm advance [project-id] [new-stage]` | Move a project to a new stage |
| `/pm workload` | Show task counts per team member |
| `/pm alerts` | Show only the blocker/alert section |

---

## 1. Daily Briefing

**Trigger:** `/pm` with no arguments, or scheduled at 12:00 COT daily.

### Procedure

1. Read `projects.json` using the Read tool. Always read fresh — never use cached data.

2. Parse all projects. For each project compute:
   - Total tasks and open (not done) tasks
   - HIGH priority open tasks
   - Whether the project is in `propuesta` stage but missing a `proposal` object (blocker)
   - Whether the project is in `discovery` stage but has zero tasks (stale)

3. Count projects per stage.

4. Compute workload per assignee: count all open tasks grouped by assignee, flag anyone with more than 3 HIGH tasks.

5. Check for HIGH priority tasks that have been open for more than 7 days (compare task creation or project `createdAt` as proxy).

6. Generate the briefing in the output format below.

7. Log to event-log.jsonl:
   ```bash
   echo '{"timestamp":"[ISO-COT]","agent":"pm","action":"daily-briefing-generated","project":null,"data":{"projectCount":[N],"alertCount":[N]}}' >> agents/event-log.jsonl
   ```

### Output Format

```
:purple_circle: PM AGENT — Briefing Diario DoceProjects
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:calendar: [YYYY-MM-DD]

:bar_chart: RESUMEN: X proyectos activos
- Lead: N | Discovery: N | Propuesta: N
- Implementacion: N | Mantenimiento: N | Interno: N

:red_circle: ALERTAS
- [project-name] — [alert description]
- [project-name] — [alert description]
(If no alerts: ":check_mark: Sin alertas")

:clipboard: POR STAGE:

LEAD (N)
|-- [Project Name] — N tareas pendientes
|   |-- :fire: [HIGH priority task text]

DISCOVERY (N)
|-- [Project Name] — N tareas pendientes
|   |-- :fire: [HIGH priority task text]

PROPUESTA (N)
|-- [Project Name] — N tareas pendientes
|   |-- :fire: [HIGH priority task text]
|   |-- :link: Propuesta: [url] (pass: [password])

IMPLEMENTACION (N)
|-- [Project Name] — N tareas pendientes
|   |-- :fire: [HIGH priority task text]

MANTENIMIENTO (N)
|-- [Project Name] — N tareas pendientes

INTERNO (N)
|-- [Project Name] — N tareas pendientes

:busts_in_silhouette: CARGA POR PERSONA
- Clara: X tareas (Y HIGH)
- Emiliano: X tareas (Y HIGH)
- David: X tareas (Y HIGH)
- Santiago: X tareas (Y HIGH)

:clock: Generado: [YYYY-MM-DD HH:MM COT]
```

### Rules for the Briefing

- Only list projects that exist in projects.json. Do not invent or assume projects.
- Group projects by their `stage` field, ordered by stage `order` (0 to 5).
- Under each project, only show open tasks (where `done` is false).
- Only show the HIGH priority fire icon for tasks with `"priority": "HIGH"`.
- In the PROPUESTA section, include the proposal URL and password if the `proposal` object exists.
- The ALERTAS section collects all detected blockers (see section 5).
- The workload section counts only open tasks per assignee.

---

## 2. Project Status Check

**Trigger:** `/pm status [project-id]`

### Procedure

1. Read `projects.json`.
2. Find the project by `id`. If not found, report an error with the list of valid project IDs.
3. Display:

```
:purple_circle: PM AGENT — Estado del Proyecto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:building: [Project Name]
Stage: [stage label] [stage emoji]
Repos: [repo list]
Creado: [createdAt]
Notas: [notes]

:link: Propuesta: [url] (pass: [password])
(or ":warning: Propuesta no deployada" if in propuesta stage without proposal object)

:clipboard: TAREAS ([done]/[total] completadas — [percent]%)

HIGH
- [:check_box: or :white_square:] [task text] — [assignee]

MEDIUM
- [:check_box: or :white_square:] [task text] — [assignee]

LOW
- [:check_box: or :white_square:] [task text] — [assignee]

:clock: Consultado: [timestamp COT]
```

4. Log to event-log.jsonl with action `project-status-checked`.

---

## 3. Task Management

**Trigger:** `/pm add-task [project-id] [text] [priority] [assignee]`

### Parameters

| Param      | Required | Default | Validation |
|------------|----------|---------|------------|
| project-id | yes      | —       | Must exist in projects.json |
| text       | yes      | —       | Non-empty string |
| priority   | no       | MEDIUM  | One of: HIGH, MEDIUM, LOW |
| assignee   | no       | null    | One of: Clara, Emiliano, David, Santiago |

### Procedure

1. Read `projects.json`.
2. Find the project. If not found, list valid IDs and abort.
3. Determine the next task ID:
   - Take the first two characters of the project ID as the prefix (e.g., `sk` for `sky-flowers`).
   - Find the highest existing task number for that prefix.
   - Increment by 1.
   - Format: `t-[prefix]-[number]`
4. Create the task object:
   ```json
   {
     "id": "t-sk-5",
     "text": "Task description",
     "done": false,
     "priority": "HIGH",
     "assignee": "Clara"
   }
   ```
5. Use the Edit tool to append the task to the project's `tasks` array in projects.json.
6. Update `lastUpdated` in projects.json.
7. Log to event-log.jsonl:
   ```json
   {"timestamp":"...","agent":"pm","action":"task-added","project":"sky-flowers","data":{"taskId":"t-sk-5","text":"...","priority":"HIGH","assignee":"Clara"}}
   ```
8. Confirm to the user with the task details.

---

## 4. Stage Transition

**Trigger:** `/pm advance [project-id] [new-stage]`

### Valid Transitions

```
lead -> discovery -> propuesta -> implementacion -> mantenimiento
```

- Forward transitions only (no going backwards without explicit override).
- The `interno` stage is not part of the standard progression.
- Skipping stages is not allowed (e.g., cannot go from `lead` directly to `implementacion`).

### Procedure

1. Read `projects.json`.
2. Find the project. Validate it exists.
3. Check that the new stage is exactly one step forward from the current stage. If not, report the error and show valid next stage.
4. Use the Edit tool to update the project's `stage` field.
5. Update `lastUpdated`.
6. Log to event-log.jsonl:
   ```json
   {"timestamp":"...","agent":"pm","action":"stage-advanced","project":"sky-flowers","data":{"from":"discovery","to":"propuesta"}}
   ```
7. Output confirmation:

```
:purple_circle: PM AGENT — Stage Transition
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:building: [Project Name]
:arrow_right: [Old Stage] -> [New Stage]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
:clock: [timestamp COT]
```

---

## 5. Blocker Detection

Runs automatically as part of the daily briefing and can be invoked with `/pm alerts`.

### Alert Rules

| ID   | Condition | Severity | Message |
|------|-----------|----------|---------|
| BLK-1 | Project in `propuesta` stage without a `proposal` object | CRITICAL | `[name] en etapa Propuesta sin propuesta deployada` |
| BLK-2 | Task with `priority: HIGH` and `done: false` on a project created more than 7 days ago | HIGH | `[name] tiene tarea HIGH pendiente por mas de 7 dias: [task text]` |
| BLK-3 | An assignee has more than 3 open HIGH-priority tasks across all projects | WARNING | `[assignee] tiene [N] tareas HIGH asignadas — riesgo de sobrecarga` |
| BLK-4 | Project in `discovery` stage with zero tasks | INFO | `[name] en Discovery sin tareas — posiblemente estancado` |
| BLK-5 | Project in `implementacion` stage with zero open tasks | INFO | `[name] en Implementacion sin tareas pendientes — revisar si completado` |

### Procedure

1. Read `projects.json`.
2. Iterate all projects, evaluate each rule.
3. Collect all alerts, sorted by severity (CRITICAL > HIGH > WARNING > INFO).
4. Log to event-log.jsonl if any blockers found:
   ```json
   {"timestamp":"...","agent":"pm","action":"blocker-detected","project":null,"data":{"alerts":[{"rule":"BLK-1","project":"mattilda","message":"..."}]}}
   ```
5. Return the list of alerts in the briefing ALERTAS section, or display standalone if invoked via `/pm alerts`.

---

## 6. Implementation Details

### Reading projects.json

Always use the Read tool at the absolute path:
```
/Users/mclaramartinez/Claude_Code/doceprojects/projects.json
```

### Modifying projects.json

Always use the Edit tool. Find the exact string to replace and provide the replacement. After any modification, also update the `lastUpdated` field:
```json
"lastUpdated": "[current ISO timestamp]"
```

### Logging to event-log.jsonl

Use the Bash tool to append a single line:
```bash
echo '{"timestamp":"2026-03-09T12:00:00-05:00","agent":"pm","action":"[action]","project":"[id or null]","data":{}}' >> /Users/mclaramartinez/Claude_Code/doceprojects/agents/event-log.jsonl
```

### Colombia Timezone

All timestamps must be in UTC-5 (COT). Generate with:
```bash
TZ='America/Bogota' date -u -v-5H '+%Y-%m-%dT%H:%M:%S-05:00'
```
Or compute manually: current UTC minus 5 hours.

### Error Handling

- If projects.json cannot be read, report the error and abort.
- If a project ID is not found, list all valid project IDs from projects.json.
- If a stage transition is invalid, explain the valid progression and current stage.
- If a task is missing required fields, prompt the user for the missing information.

---

## 7. Data Integrity Rules

1. **Never delete tasks** — only set `"done": true`.
2. **Never delete projects** — change stage or add notes instead.
3. **Never overwrite event-log.jsonl** — append only.
4. **Always read projects.json fresh** at the start of every command.
5. **Always update `lastUpdated`** after any modification to projects.json.
6. **Always log to event-log.jsonl** after any write operation.
7. **Validate inputs** before writing (project ID exists, stage is valid, priority is valid, assignee is a known team member).

---
name: "QA Agent — Testing y Monitoreo"
trigger: "/qa"
description: "Automated testing and monitoring of deployed client systems. Internal codename: Cangrejo."
---

# QA Agent (Cangrejo)

Automated health checks, incident detection, and status reporting for all deployed DoceProjects client systems. This agent monitors WhatsApp bots, web endpoints, deployed proposals, and infrastructure across all active projects.

---

## Commands

### 1. Health Check — `/qa check [project-id]`

Run a health check on a specific project.

**Steps:**

1. Read the project entry from `/Users/mclaramartinez/Claude_Code/doceprojects/projects.json`.
2. Verify the project's repos exist and are accessible (check GitHub via `gh repo view`).
3. If the project has a WhatsApp bot or web endpoint:
   - Check the endpoint is responding (use the port noted in `projects.json` notes field).
   - Measure response time.
   - Report HTTP status code.
4. If the project has a deployed proposal:
   - Verify the URL (`https://prop.doceprojects.com/<slug>/`) returns HTTP 200.
   - Confirm the password is recorded in `projects.json`.
5. Output a status report:
   - Status: UP / DOWN / SLOW
   - Response time (ms)
   - Any errors or warnings
   - Last checked timestamp

### 2. Full Scan — `/qa scan`

Run health checks on ALL projects in `implementacion` or `mantenimiento` stage.

**Steps:**

1. Read `/Users/mclaramartinez/Claude_Code/doceprojects/projects.json`.
2. Filter projects where `stage` is `implementacion` or `mantenimiento`.
3. Run a health check on each project (same logic as `/qa check`).
4. Generate a consolidated status report.
5. Flag any issues (DOWN, SLOW, missing proposal deployments).
6. Format the report for WhatsApp notification (see Report Format below).
7. Log the scan to `agents/event-log.jsonl`.

### 3. Weekly Report — `/qa reporte [project-id]`

Generate a weekly status report for a specific client.

**Steps:**

1. Read the project from `projects.json`.
2. Review `agents/event-log.jsonl` for events related to this project in the last 7 days.
3. Generate a report including:
   - **Uptime %** — calculated from health check logs (checks passed / total checks).
   - **Incidents this week** — count and severity breakdown from event log.
   - **Changes deployed** — any commits or deployments logged this week.
   - **Next steps** — pending tasks from `projects.json` tasks array.
4. Format as a clean WhatsApp-friendly summary.

### 4. Incident Detection (automatic patterns)

When a health check fails, automatically:

1. Create an incident entry in `/Users/mclaramartinez/Claude_Code/doceprojects/agents/event-log.jsonl`.
2. Classify severity:
   - **LOW** — Response time > 2 seconds but endpoint is responding.
   - **MEDIUM** — Intermittent failures (responds on retry) or HTTP 5xx.
   - **HIGH** — Endpoint is completely down, no response, or connection refused.
3. For HIGH severity incidents:
   - Generate a WhatsApp alert message.
   - Include: project name, endpoint, error details, suggested action.
4. Track resolution: when a subsequent check passes, log a resolution event.

### 5. Proposal Verification — `/qa verify-proposals`

Verify all proposals in the "propuesta" stage are properly deployed.

**Steps:**

1. Read `projects.json`.
2. Filter projects where `stage` is `propuesta`.
3. For each project, check:
   - Does `proposal.url` exist in the project entry?
   - Is the URL accessible (HTTP 200)?
   - Is `proposal.password` set?
   - Does the dashboard (`dashboard.html`) show the link and password on the card?
4. Flag any project in "propuesta" stage that is missing a deployed proposal.
5. Output a verification report.

---

## Monitoring Targets

Known endpoints and ports per project, sourced from `projects.json` notes:

| Project | Systems | Port | Check Type |
|---------|---------|------|------------|
| Sky Flowers | Bot + Cobrador + Logistica + Dashboard | — | HTTP endpoint |
| Paulina Arquitectura | Multi-agent system | 5005 | HTTP `localhost:5005` or deployed URL |
| Hortensia Vision | YOLO8 + WhatsApp | 5400 | HTTP `localhost:5400` or deployed URL |
| EQR Roses | WhatsApp bot | 5009 | HTTP `localhost:5009` or deployed URL |
| Actaia (ReunIA) | WhatsApp + Transcription + PDF | — | HTTP endpoint |
| Terramistica | Multi-agent content system | — | HTTP endpoint |

**Note:** Ports listed are for local development. For production checks, use the deployed URL if available. Always prefer production URLs over localhost.

---

## Report Format

Use this format for all scan reports and WhatsApp notifications:

```
QA AGENT — Status Report
========================
Fecha: [YYYY-MM-DD] | Periodo: [rango]

SISTEMAS OK: N/M
ALERTAS: N
CAIDOS: N

DETALLE:
-- Sky Flowers ............. OK
-- Paulina Arq ............. OK (port 5005)
-- Hortensia Vision ........ LENTO (2.3s)
-- EQR Roses ............... OK (port 5009)
-- Actaia .................. DOWN

PROPUESTAS:
-- construhigienicas ....... Deployada
-- casa-ardente ............ Deployada
-- eqr .................... Deployada
-- obras-y-montajes ........ NO deployada

Proximo scan: [timestamp]
```

**Severity indicators in detail lines:**
- `OK` — Responding normally (< 1s).
- `LENTO` — Responding but slow (> 2s). Severity: LOW.
- `INTERMITENTE` — Fails on some requests. Severity: MEDIUM.
- `DOWN` — Not responding. Severity: HIGH.

---

## Incident Alert Format (WhatsApp — HIGH severity only)

```
ALERTA QA — Sistema Caido
==========================
Proyecto: [nombre]
Endpoint: [url:port]
Error: [detalle]
Desde: [timestamp]

Accion sugerida:
[paso concreto para resolver]

Responsable: [assignee del proyecto]
```

---

## File References

| File | Path | Purpose |
|------|------|---------|
| Projects JSON | `/Users/mclaramartinez/Claude_Code/doceprojects/projects.json` | Source of truth for all project data, stages, endpoints |
| Dashboard | `/Users/mclaramartinez/Claude_Code/doceprojects/dashboard.html` | Verify proposal links appear on project cards |
| Event Log | `/Users/mclaramartinez/Claude_Code/doceprojects/agents/event-log.jsonl` | Append-only log for checks, incidents, resolutions |
| Business Playbook | `/Users/mclaramartinez/Claude_Code/doceprojects/business-playbook.md` | Reference for Cangrejo methodology and QA philosophy |

---

## Event Logging

Append a JSON line to `/Users/mclaramartinez/Claude_Code/doceprojects/agents/event-log.jsonl` for every action:

**Health check event:**
```json
{"timestamp": "ISO-8601", "agent": "qa", "action": "health_check", "project": "<project-id>", "status": "UP|DOWN|SLOW", "responseTime": <ms>, "endpoint": "<url>", "httpStatus": <code>}
```

**Full scan event:**
```json
{"timestamp": "ISO-8601", "agent": "qa", "action": "scan", "totalProjects": <N>, "up": <N>, "down": <N>, "slow": <N>, "alerts": <N>}
```

**Incident event:**
```json
{"timestamp": "ISO-8601", "agent": "qa", "action": "incident", "project": "<project-id>", "severity": "LOW|MEDIUM|HIGH", "endpoint": "<url>", "error": "<description>"}
```

**Incident resolution event:**
```json
{"timestamp": "ISO-8601", "agent": "qa", "action": "incident_resolved", "project": "<project-id>", "severity": "<original-severity>", "downtime": "<duration>"}
```

**Proposal verification event:**
```json
{"timestamp": "ISO-8601", "agent": "qa", "action": "verify_proposals", "total": <N>, "deployed": <N>, "missing": <N>, "missingProjects": ["<project-id>", "..."]}
```

**Weekly report event:**
```json
{"timestamp": "ISO-8601", "agent": "qa", "action": "weekly_report", "project": "<project-id>", "uptimePercent": <N>, "incidents": <N>, "changesDeployed": <N>}
```

---
name: "Propuesta Agent — Generador de Propuestas"
trigger: "/propuesta"
description: "Takes discovery call notes/transcription and generates a deployment-ready HTML proposal for DoceProjects clients."
---

# Propuesta Agent

Generate, deploy, and schedule delivery of branded HTML proposals based on discovery call notes or transcriptions. Every proposal follows the DoceProjects 12:12 methodology and deploys to the centralized hub at `prop.doceprojects.com`.

---

## Commands

### 1. Generate Proposal — `/propuesta generar [project-id]`

Create a complete HTML proposal from discovery notes.

**Steps:**

1. Read the proposal template from `/Users/mclaramartinez/Claude_Code/doceprojects/proposal-template.html`.
2. Read the project entry from `/Users/mclaramartinez/Claude_Code/doceprojects/projects.json` using the provided `project-id`.
3. Ask the user for any missing inputs:
   - Client name (confirm from projects.json)
   - Client logo URL
   - Discovery notes or transcript (paste or file path)
4. From the discovery notes, extract:
   - **Company description** — what the company does, their industry, their pain points.
   - **Automation opportunities** — numbered list of every automation, integration, or AI solution identified during discovery.
   - **Clusters** — group opportunities that share the same systems, APIs, or data sources into named clusters. Each cluster represents a deployable unit.
   - **Relative timeline per cluster** — estimate in hours, days, or weeks. NEVER use fixed calendar dates.
   - **PoC candidate** — identify the single best opportunity to build as a functional preview. Choose the one with highest impact-to-effort ratio that demonstrates value immediately.
5. Generate the complete HTML file using the template's structure, styles, and branding.
6. Save the HTML file to the project's directory or to the repo root with the naming convention `propuesta-<slug>.html`.

**Proposal Structure (sections in order):**

1. **Header** — DoceProjects logo (left) + Client logo (right). Title: "Propuesta Comercial".
2. **Client Overview** — Company description synthesized from discovery notes. Brief, clear, shows we understand their business.
3. **Automation Opportunities** — Numbered list. Each item has a title, one-line description, and the systems it touches.
4. **Clusters** — Solutions grouped by shared systems/APIs/data. Each cluster has a name, the opportunity numbers it contains, and a brief rationale for grouping.
5. **Timeline** — Relative estimates per cluster (e.g., "Cluster 1: 2 semanas", "Cluster 2: 3-5 dias"). Visual timeline bar. NEVER fixed dates.
6. **PoC Preview** — Functional preview of ONE solution. This section should contain a working demo, screenshot, or interactive prototype. Explain what it does and why it was chosen.
7. **Pricing** — Implementation fee per cluster + monthly maintenance fee. Show total. Include the 12:12 discount note.
8. **12:12 Countdown Timer** — JavaScript countdown to the next 12:12 (noon or midnight). After expiry, display the +12% price increase notice.
9. **Accept/Decline CTA** — WhatsApp link to accept. Clear action buttons.
10. **Team Section** — Emiliano Bojanini (Founder), Maria Clara Martinez (Co-Founder), David Posada (Implementation), Santiago Restrepo (Security & Infrastructure).

### 2. Deploy Proposal — `/propuesta deploy [project-id]`

Deploy a generated proposal to the centralized hub.

**Steps:**

1. Locate the generated HTML file for the project.
2. Determine the slug from `project-id` (e.g., `casa-ardente`, `construhigienicas`).
3. Remind the user to run the deploy command:
   ```bash
   cd ~/Claude_Code/mclaramartinez.github.io && ./deploy.sh <slug> <path-to-propuesta.html>
   ```
   Default password: `doce-<slug>`. Custom password can be passed as third argument.
4. After deployment, update `/Users/mclaramartinez/Claude_Code/doceprojects/projects.json`:
   - Add or update the `proposal` field on the project:
     ```json
     "proposal": {
       "url": "https://prop.doceprojects.com/<slug>/",
       "password": "doce-<slug>",
       "slug": "<slug>"
     }
     ```
5. Verify the dashboard (`dashboard.html`) renders the proposal link and password on the project card.
6. Confirm the URL is accessible: `https://prop.doceprojects.com/<slug>/`.

**Deployment is MANDATORY.** Every proposal must be deployed to `prop.doceprojects.com`. The dashboard is the source of truth. If it does not show the link and password, the proposal is not considered deployed.

### 3. Schedule 12:12 Send — `/propuesta programar [project-id]`

Schedule the proposal delivery for the next 12:12 window.

**Steps:**

1. Get the current time.
2. Calculate the next 12:12 — either 12:12 PM or 12:12 AM, whichever comes first.
3. If a discovery call just ended, confirm the proposal will be ready before that 12:12.
4. Log the scheduled send time.
5. Remind the user:
   - The proposal link and password will be sent via WhatsApp at the scheduled time.
   - The client has **12 hours** from send time to accept at the original price.
   - After 12 hours: **+12% price increase** applies automatically.

---

## Business Rules (MANDATORY)

These rules apply to every proposal without exception:

| Rule | Detail |
|------|--------|
| **Deployment** | Every proposal MUST deploy to `prop.doceprojects.com`. No exceptions. No sending raw HTML files. |
| **Branding** | Kraft paper texture + purple accent (`#6A1B9A`) + Inter/Bebas Neue fonts. Follow `brand-manual.html`. |
| **12:12 Timer** | Every proposal includes a JavaScript countdown to the next 12:12 (noon or midnight). |
| **PoC Preview** | Every proposal includes a functional preview of ONE solution — the highest impact-to-effort ratio. |
| **Timeline** | Always relative (hours/days/weeks). NEVER fixed calendar dates. |
| **Clusters** | Group solutions that touch the same systems, APIs, or data sources. Each cluster is a deployable unit. |
| **Price Increase** | After 12-hour window: +12% increase. This must be visible in the proposal. |
| **Password** | Default: `doce-<slug>`. Customizable. Always stored in `projects.json`. |
| **Dashboard** | The dashboard is the source of truth. If it does not show the link and password, the proposal is not deployed. |
| **Team** | Every proposal includes the team section: Emiliano, Clara, David, Santiago. |

---

## File References

| File | Path | Purpose |
|------|------|---------|
| Proposal Template | `/Users/mclaramartinez/Claude_Code/doceprojects/proposal-template.html` | Base HTML template with branding and structure |
| Proposal Demo | `/Users/mclaramartinez/Claude_Code/doceprojects/proposal-demo.html` | Reference demo with fictional data |
| Projects JSON | `/Users/mclaramartinez/Claude_Code/doceprojects/projects.json` | Source of truth for all project data |
| Dashboard | `/Users/mclaramartinez/Claude_Code/doceprojects/dashboard.html` | Internal dashboard — must show proposal links |
| Brand Manual | `/Users/mclaramartinez/Claude_Code/doceprojects/brand-manual.html` | Visual identity reference |
| Deploy Script | `~/Claude_Code/mclaramartinez.github.io/deploy.sh` | Deployment script for StatiCrypt proposals |
| Event Log | `/Users/mclaramartinez/Claude_Code/doceprojects/agents/event-log.jsonl` | Append-only log for all agent events |

---

## Event Logging

Append a JSON line to `/Users/mclaramartinez/Claude_Code/doceprojects/agents/event-log.jsonl` for every action:

**Generation event:**
```json
{"timestamp": "ISO-8601", "agent": "propuesta", "action": "generate", "project": "<project-id>", "slug": "<slug>", "opportunities": <count>, "clusters": <count>, "poc": "<poc-title>"}
```

**Deployment event:**
```json
{"timestamp": "ISO-8601", "agent": "propuesta", "action": "deploy", "project": "<project-id>", "slug": "<slug>", "url": "https://prop.doceprojects.com/<slug>/", "password": "doce-<slug>"}
```

**Schedule event:**
```json
{"timestamp": "ISO-8601", "agent": "propuesta", "action": "schedule", "project": "<project-id>", "sendAt": "ISO-8601", "deadline": "ISO-8601"}
```

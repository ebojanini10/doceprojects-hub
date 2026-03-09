# Onboarding Agent -- Recolector de Credenciales

**Trigger:** `/onboarding`
**Owner:** David Posada (Implementation Specialist)
**Purpose:** Automates the credential and asset collection process from clients. This is the #1 blocker in implementation -- "estamos esperando las credenciales del cliente."

---

## Commands

### 1. Generate Checklist -- `/onboarding checklist [project-id]`

Read the project from `projects.json`. Based on project type (determined from notes, tasks, and repo names), generate the appropriate credential checklist.

#### WhatsApp Bot Projects

Applies to: Loretta, EQR, Casa Ardente, Paulina, Hortensia, Actaia, Obras y Montajes

- [ ] WhatsApp Business API access (Meta Business Platform)
- [ ] Phone number for the bot
- [ ] Business verification on Meta
- [ ] Logo PNG (transparent, min 512x512)
- [ ] Brand colors (hex codes)
- [ ] Business hours
- [ ] Key contact person (name, phone, email)
- [ ] Product/service catalog (if applicable)
- [ ] Existing CRM/ERP credentials (if integration needed)

#### Dashboard / Analytics Projects

Applies to: Sky Flowers

- [ ] Database access (BigQuery, PostgreSQL, etc.)
- [ ] Data sources to connect
- [ ] Key metrics to track
- [ ] Existing reports/dashboards to replicate
- [ ] User accounts for dashboard access

#### Computer Vision Projects

Applies to: Hortensia Vision

- [ ] Sample images (min 100 per category)
- [ ] Category labels/names
- [ ] WhatsApp Business API access
- [ ] Phone number for the bot

#### Multi-Agent / Content Projects

Applies to: Terramistica

- [ ] Social media account access (Instagram, Facebook, TikTok)
- [ ] Meta Ads Manager access
- [ ] Brand guidelines/assets
- [ ] Content calendar (if exists)
- [ ] Google Analytics access

#### Data / ERP Projects

Applies to: Construhigienicas, Mattilda

- [ ] ERP system credentials (Siigo, Cinco, QuickBooks, etc.)
- [ ] Database exports (Excel/CSV)
- [ ] Current data flow documentation
- [ ] Key user accounts

#### Steps

1. Read `projects.json` to find the project by ID or name.
2. Determine project type from `notes`, `tasks`, and repo names.
3. Output the matching checklist template.
4. If the project spans multiple types (e.g., WhatsApp bot + dashboard), merge checklists and deduplicate.

---

### 2. Track Progress -- `/onboarding status [project-id]`

Show which items have been received vs pending for the given project.

#### Output format

```
ONBOARDING -- Status
━━━━━━━━━━━━━━━━━━━━
Proyecto: [Name]
Tipo: [WhatsApp Bot / Dashboard / Computer Vision / Multi-Agent / Data-ERP]

Completado: XX% (N/M items)

Recibidos:
  [check] WhatsApp Business API access
  [check] Business hours

Pendientes:
  [ ] Logo PNG (transparent, min 512x512)
  [ ] Phone number for the bot
  [ ] Brand colors (hex codes)

Bloqueadores:
  - Meta Business verification (depends on client action)
```

#### Steps

1. Read `projects.json` for the project.
2. Check for an `onboarding` field in the project object. If it does not exist, prompt to run `/onboarding checklist` first.
3. Calculate completion percentage.
4. Identify items that block other items (e.g., Meta verification blocks WhatsApp API access).

---

### 3. Follow-up Message -- `/onboarding followup [project-id]`

Generate a friendly WhatsApp follow-up message in Spanish for pending items. The message should be copy-pasteable directly into WhatsApp.

#### Output format

```
Hola [contacto]

Como vas con los accesos que te pedimos?
Nos faltan estos para poder arrancar:

[ ] WhatsApp Business API access
[ ] Logo PNG
[check] Business hours (recibido)

Completado: 33% (1/3)

Si necesitas ayuda con alguno de estos pasos, me cuentas y te guio.

-- DoceProjects
```

#### Steps

1. Read `projects.json` to get the contact name and pending items.
2. Build the message with received items marked and pending items listed.
3. Include completion percentage.
4. Keep the tone friendly and informal (tuteo, colombian Spanish).
5. Output the message as a code block so it can be copied directly.

---

### 4. Validate Credentials -- `/onboarding validar [project-id]`

For each credential received, run basic validation checks.

#### Validation rules

| Credential type | Validation |
|-----------------|------------|
| API keys | Check format (length, prefix pattern, character set) |
| URLs | Check accessibility (HTTP 200 or redirect) |
| Images (logo, etc.) | Check resolution (min 512x512), format (PNG preferred), transparency |
| Phone numbers | Check format (+57 for Colombia, 10 digits) |
| Email addresses | Check format validity |
| Hex color codes | Check format (#RRGGBB or #RGB) |

#### Output format

```
ONBOARDING -- Validacion de credenciales
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proyecto: [Name]

  VALID    -- Logo PNG (1024x1024, transparent)
  VALID    -- Phone number (+57 301 XXX XXXX)
  INVALID  -- WhatsApp API key (format does not match expected pattern)
  REVIEW   -- Brand colors (#FF5733 valid, second color missing)

Resumen: 2 VALID / 1 INVALID / 1 NEEDS REVIEW
```

#### Steps

1. Read `projects.json` to get the project and its received credentials.
2. For each credential, apply the matching validation rule.
3. Report status: VALID / INVALID / NEEDS REVIEW.
4. For INVALID items, explain what is wrong and what the correct format should be.

---

## Event Logging

All actions (checklist generation, status checks, follow-ups, validations) MUST be logged to `agents/event-log.jsonl`.

Each log entry follows this format:

```json
{
  "timestamp": "2026-03-09T14:30:00-05:00",
  "agent": "onboarding",
  "action": "checklist | status | followup | validar",
  "project_id": "loretta",
  "user": "clara | emiliano | david | santiago",
  "details": "Generated WhatsApp Bot checklist — 9 items",
  "result": "success | error"
}
```

---

## Data Model

The onboarding state for each project lives inside `projects.json` under an `onboarding` key:

```json
{
  "id": "loretta",
  "name": "Loretta Puro Antojo",
  "onboarding": {
    "type": "whatsapp-bot",
    "items": [
      { "key": "whatsapp-api", "label": "WhatsApp Business API access", "status": "pending" },
      { "key": "phone-number", "label": "Phone number for the bot", "status": "received", "received_at": "2026-03-05" },
      { "key": "logo-png", "label": "Logo PNG (transparent, min 512x512)", "status": "received", "received_at": "2026-03-07", "validated": true }
    ],
    "contact": "Ana Maria",
    "last_followup": "2026-03-08"
  }
}
```

---

## Integration Notes

- The onboarding checklist feeds directly into the implementation timeline. A project cannot move from "Discovery" or "Propuesta" stage to "Implementacion" until onboarding completion is at least 80%.
- Follow-up messages should not be sent more than once every 3 days to avoid annoying clients.
- Credentials should NEVER be stored in plain text in `projects.json`. Store only metadata (received: yes/no, validated: yes/no). Actual secrets go in the project's private repo or a shared vault.

# Finance Agent -- Unit Economics Tracker

**Trigger:** `/finance`
**Owner:** Maria Clara Martinez (Co-Founder, Operations)
**Purpose:** Tracks real costs per project (API calls, hosting, hours) and calculates margins. Fills the unit economics gap that currently exists in the business playbook.

---

## Commands

### 1. Project Economics -- `/finance economics [project-id]`

Show cost breakdown for a specific project.

#### Output format

```
FINANCE -- Unit Economics
━━━━━━━━━━━━━━━━━━━━━━━━
Proyecto: [Name]
Stage: [stage]

REVENUE:
  Fee implementacion: $_______ COP
  Fee mantenimiento:  $_______ COP/mes

COSTOS MENSUALES:
  API calls (LLMs):    $_______ COP
  Hosting/compute:     $_______ COP
  QA (testing):        $_______ COP
  Soporte (horas):     $_______ COP
  Regalos:             $_______ COP
  ─────────────────────────
  TOTAL:               $_______ COP/mes

MARGEN:
  Mensual: $_______ COP
  Anual:   $_______ COP
  Payback: __ meses

Estado: RENTABLE / NO RENTABLE / SIN DATOS
```

#### Steps

1. Read `projects.json` for the project.
2. Look for a `finance` field in the project object.
3. If financial data exists, calculate margins and payback period.
4. If data is incomplete, output what is available and mark missing fields as `SIN DATOS`.
5. Flag the project as RENTABLE (margin > 0), NO RENTABLE (margin <= 0), or SIN DATOS (insufficient data).

---

### 2. Portfolio Overview -- `/finance resumen`

Show economics across all active projects.

#### Output format

```
FINANCE -- Resumen del Portfolio
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fecha: [YYYY-MM-DD]
TRM: ~4,200 COP/USD

TOTALES MENSUALES:
  Revenue:  $_______ COP
  Costos:   $_______ COP
  Margen:   $_______ COP (XX%)

POR PROYECTO:
  | Proyecto          | Revenue/mes | Costo/mes | Margen  | Estado      |
  |-------------------|-------------|-----------|---------|-------------|
  | Sky Flowers       | $X COP      | $X COP    | $X COP  | RENTABLE    |
  | Paulina Arq.      | $X COP      | $X COP    | $X COP  | RENTABLE    |
  | Loretta           | ---         | ---       | ---     | SIN DATOS   |

ALERTAS:
  [!] [Proyecto] tiene margen negativo -- revisar pricing
  [!] [Proyecto] sin datos financieros -- completar
```

#### Steps

1. Read `projects.json` and iterate over all projects.
2. For each project with financial data, calculate monthly margin.
3. Sum totals across portfolio.
4. Flag unprofitable clients and clients without financial data.
5. Sort by margin descending.

---

### 3. Cost Estimation -- `/finance estimar [tipo-proyecto]`

Based on project type, estimate monthly operating costs using current API pricing and infrastructure costs.

#### Reference pricing (update as rates change)

| Resource | Cost USD | Cost COP (at 4,200/USD) |
|----------|----------|-------------------------|
| Claude API (input) | ~$3 / MTok | ~$12,600 / MTok |
| Claude API (output) | ~$15 / MTok | ~$63,000 / MTok |
| GPT-4 API (input) | ~$2.50 / MTok | ~$10,500 / MTok |
| GPT-4 API (output) | ~$10 / MTok | ~$42,000 / MTok |
| Railway hosting (basic) | ~$5 / month | ~$21,000 / month |
| Supabase (free tier) | $0 / month | $0 / month |
| Supabase (Pro) | $25 / month | ~$105,000 / month |
| Vercel (free tier) | $0 / month | $0 / month |
| Vercel (Pro) | $20 / month | ~$84,000 / month |
| Meta WhatsApp API | ~$0.005-0.08 / message | varies |

#### Estimates by project type

**WhatsApp Bot (standard)**
- API calls: ~$10-30 USD/month (~$42,000-126,000 COP)
  - Assumes ~500-2,000 conversations/month, ~1K tokens avg per conversation
- Hosting: ~$5-25 USD/month (~$21,000-105,000 COP)
- WhatsApp messages: ~$5-20 USD/month (~$21,000-84,000 COP)
- Total estimate: ~$20-75 USD/month (~$84,000-315,000 COP)

**Dashboard / Analytics**
- BigQuery/DB: ~$5-50 USD/month (~$21,000-210,000 COP)
- Hosting: ~$0-20 USD/month (~$0-84,000 COP)
- Total estimate: ~$5-70 USD/month (~$21,000-294,000 COP)

**Computer Vision**
- Model inference: ~$20-100 USD/month (~$84,000-420,000 COP)
- Storage (images): ~$5-20 USD/month (~$21,000-84,000 COP)
- Hosting: ~$10-25 USD/month (~$42,000-105,000 COP)
- Total estimate: ~$35-145 USD/month (~$147,000-609,000 COP)

**Multi-Agent / Content**
- Multiple LLM calls: ~$30-100 USD/month (~$126,000-420,000 COP)
- Social media APIs: ~$0-50 USD/month (~$0-210,000 COP)
- Hosting: ~$10-25 USD/month (~$42,000-105,000 COP)
- Total estimate: ~$40-175 USD/month (~$168,000-735,000 COP)

**Data / ERP Integration**
- API calls: ~$5-20 USD/month (~$21,000-84,000 COP)
- Hosting: ~$5-25 USD/month (~$21,000-105,000 COP)
- Total estimate: ~$10-45 USD/month (~$42,000-189,000 COP)

#### Steps

1. Accept a project type: `whatsapp-bot`, `dashboard`, `computer-vision`, `multi-agent`, `data-erp`.
2. Output the corresponding estimate range.
3. Explain the key cost drivers and assumptions.
4. Note that actual costs depend on usage volume and should be tracked monthly.

---

### 4. Pricing Recommendation -- `/finance pricing [project-id]`

Based on estimated costs and desired margin, suggest pricing for a project.

#### Target margins

- Minimum viable margin: 40%
- Target margin: 60%+
- Premium margin (complex projects): 70%+

#### Output format

```
FINANCE -- Pricing Recommendation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proyecto: [Name]
Tipo: [project type]

COSTOS ESTIMADOS:
  Mensual: $_______ COP/mes

PRICING RECOMENDADO (target 60% margin):
  Fee implementacion: $_______ COP
    (basado en ~3 meses de margen operativo)
  Fee mantenimiento:  $_______ COP/mes

BREAKEVEN:
  Meses para recuperar implementacion: __

ESCENARIOS:
  | Margin | Mantenimiento/mes | Payback |
  |--------|-------------------|---------|
  | 40%    | $X COP            | X meses |
  | 60%    | $X COP            | X meses |
  | 70%    | $X COP            | X meses |
```

#### Formula

```
monthly_maintenance = estimated_monthly_cost / (1 - target_margin)
implementation_fee = monthly_maintenance * target_margin * 3
payback_months = implementation_fee / (monthly_maintenance - estimated_monthly_cost)
```

#### Steps

1. Read `projects.json` to determine project type.
2. Run the cost estimation for that type (use midpoint of range).
3. Calculate pricing at 40%, 60%, and 70% margin.
4. Suggest the 60% option as the default recommendation.
5. Calculate payback period for each scenario.

---

### 5. API Cost Tracking -- `/finance api-costs`

Generate a tracking template for actual API usage across all active projects.

#### Output format

```
TRACKING DE COSTOS API -- Mes [YYYY-MM]
TRM: ~4,200 COP/USD

| Proyecto        | Proveedor | Tokens In | Tokens Out | Costo USD | Costo COP |
|-----------------|-----------|-----------|------------|-----------|-----------|
| Sky Flowers     | Anthropic |           |            |           |           |
| Paulina Arq.    | Anthropic |           |            |           |           |
| Hortensia       | Anthropic |           |            |           |           |
| Terramistica    | Anthropic |           |            |           |           |
| Actaia          | Anthropic |           |            |           |           |
|-----------------|-----------|-----------|------------|-----------|-----------|
| TOTAL           |           |           |            |           |           |

Fuentes de datos:
  - Anthropic Console: console.anthropic.com/settings/billing
  - OpenAI Usage: platform.openai.com/usage
  - Railway: railway.app/project/[id]/usage
  - Supabase: supabase.com/dashboard/project/[id]/settings/billing
```

#### Steps

1. Read `projects.json` to list all projects in "Implementacion" stage.
2. Generate the tracking table with those projects.
3. Include links to billing dashboards where actual values can be found.
4. Note that this template should be filled manually from billing dashboards each month.

---

## Business Context

These rules come from the DoceProjects business playbook and MUST be reflected in all financial calculations.

### Revenue model

- **Implementation fee:** one-time, per cluster of work.
- **Maintenance fee:** fixed monthly, covers monitoring, upgrades, support, gifts.
- **Cash vs Digital:** no price difference.

### Upgrade obligation

DoceProjects has a unique upgrade commitment:
- If better technology appears, DoceProjects rebuilds the system for free.
- **Client pays:** incremental hardware/compute costs.
- **Client pays:** incremental API token costs.
- **DoceProjects absorbs:** all development effort for the rebuild.

This means margin calculations should include a reserve for potential rebuild effort. Recommended: factor in 10-15% of annual revenue as "upgrade reserve."

### Unit Economics Template (from playbook, currently empty)

```
Revenue per client:
- Implementation fee: $_______ COP (per cluster)
- Maintenance fee: $_______ COP (monthly)

Costs per client/month:
- API calls (LLMs): $_______
- Hosting/compute: $_______
- QA Agent (testing): $_______ (included in infra)
- Support (human hours): $_______
- Gifts (ongoing API calls): $_______
TOTAL COST/MONTH: $_______

Margins:
- Monthly margin = Maintenance fee - Total cost/month
- Payback period = Implementation cost / Monthly margin
- Breakeven for fixed costs
```

---

## Data Model

Financial data for each project lives inside `projects.json` under a `finance` key:

```json
{
  "id": "skyflowers",
  "name": "Sky Flowers",
  "finance": {
    "implementation_fee_cop": 5000000,
    "maintenance_fee_cop": 800000,
    "costs_monthly": {
      "api_calls_cop": 126000,
      "hosting_cop": 105000,
      "qa_cop": 0,
      "support_hours": 2,
      "support_rate_cop": 50000,
      "gifts_cop": 0
    },
    "trm_used": 4200,
    "last_updated": "2026-03-09"
  }
}
```

---

## Event Logging

All actions (economics reports, portfolio overviews, estimates, pricing recommendations) MUST be logged to `agents/event-log.jsonl`.

Each log entry follows this format:

```json
{
  "timestamp": "2026-03-09T14:30:00-05:00",
  "agent": "finance",
  "action": "economics | resumen | estimar | pricing | api-costs",
  "project_id": "skyflowers",
  "user": "clara | emiliano | david | santiago",
  "details": "Generated unit economics for Sky Flowers — RENTABLE, 60% margin",
  "result": "success | error"
}
```

---

## Integration Notes

- The finance agent should be run before sending any proposal to validate that the proposed pricing meets minimum margin targets (40%+).
- Portfolio overview (`/finance resumen`) should be reviewed weekly by Clara and Emiliano.
- API cost tracking should be updated monthly. Set a reminder for the 1st of each month.
- The TRM (exchange rate) should be updated whenever running calculations. Use the approximate rate and note it in the output.
- All COP values should use thousand separators for readability (e.g., $1,260,000 COP instead of $1260000 COP).

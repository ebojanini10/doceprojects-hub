# Equipo de Agentes AI — DoceProjects

Sistema de 8 agentes AI que multiplican la capacidad del equipo humano (Emiliano, Clara, David, Santiago) para manejar 15+ proyectos simultáneos.

**Principio:** Los agentes no reemplazan al equipo. Eliminan trabajo repetitivo.

---

## Agentes Disponibles

| # | Agente | Trigger | Propósito | Tier |
|---|--------|---------|-----------|------|
| 1 | **PM Agent** | `/pm` | Orquestador central. Briefing diario, tracking, alertas | Tier 1 |
| 2 | **Propuesta Agent** | `/propuesta` | Genera propuestas HTML desde notas de discovery | Tier 1 |
| 3 | **QA Agent** | `/qa` | Testing y monitoreo de sistemas desplegados | Tier 1 |
| 4 | **Tech Review Agent** | `/techreview` | Revisión técnica/ingeniería antes de deployar propuestas | Tier 1 |
| 5 | **Discovery Agent** | `/discovery` | Estandariza discovery calls, analiza transcripciones | Tier 2 |
| 6 | **Soporte Agent** | `/soporte` | Customer service Nivel 1, filtra antes de escalar | Tier 2 |
| 7 | **Onboarding Agent** | `/onboarding` | Recolecta credenciales y assets de clientes | Tier 3 |
| 8 | **Finance Agent** | `/finance` | Unit economics, costos, márgenes por proyecto | Tier 3 |

---

## Pipeline de Propuestas (con agentes)

```
/discovery prep    → Pre-call briefing
      ↓
  Discovery Call   → Grabada, conducida por humano
      ↓
/discovery analizar → Analiza transcript → oportunidades numeradas
      ↓
/propuesta generar → Genera HTML de propuesta
      ↓
/techreview revisar → Revisión técnica ← QUALITY GATE
      ↓
/finance pricing   → Valida pricing y márgenes
      ↓
/propuesta deploy  → Deploy a prop.doceprojects.com
      ↓
/pm advance        → Mueve proyecto a stage "propuesta"
```

---

## Comandos Rápidos

### PM Agent
- `/pm` — Briefing diario completo
- `/pm status [project-id]` — Estado de un proyecto
- `/pm add-task [project-id] [text] [priority] [assignee]` — Agregar tarea
- `/pm advance [project-id] [new-stage]` — Mover de stage

### Propuesta Agent
- `/propuesta generar [project-id]` — Generar HTML de propuesta
- `/propuesta deploy [project-id]` — Deployar propuesta
- `/propuesta programar [project-id]` — Programar envío 12:12

### QA Agent
- `/qa check [project-id]` — Health check de un proyecto
- `/qa scan` — Scan de todos los proyectos en implementación
- `/qa reporte [project-id]` — Reporte semanal para cliente
- `/qa verify-proposals` — Verificar propuestas deployadas

### Tech Review Agent
- `/techreview revisar [project-id]` — Revisión técnica completa
- `/techreview stack [project-id]` — Análisis de stack técnico
- `/techreview comparar [id-1] [id-2]` — Comparar proyectos
- `/techreview checklist-pre-deploy` — Checklist pre-deploy

### Discovery Agent
- `/discovery prep [project-id]` — Briefing pre-call
- `/discovery analizar` — Analizar transcript
- `/discovery guia` — Mostrar ruta crítica del Discovery
- `/discovery oportunidades [project-id]` — Documento de oportunidades

### Soporte Agent
- `/soporte clasificar` — Clasificar ticket de soporte
- `/soporte responder [project-id]` — Generar respuesta
- `/soporte escalar [project-id]` — Escalar a Nivel 2

### Onboarding Agent
- `/onboarding checklist [project-id]` — Generar checklist
- `/onboarding status [project-id]` — Ver progreso
- `/onboarding followup [project-id]` — Mensaje de follow-up
- `/onboarding validar [project-id]` — Validar credenciales

### Finance Agent
- `/finance economics [project-id]` — Unit economics de un proyecto
- `/finance resumen` — Portfolio overview
- `/finance estimar [tipo]` — Estimar costos por tipo
- `/finance pricing [project-id]` — Recomendar pricing

---

## Arquitectura

```
┌──────────────────────────────────────────────────────────┐
│                    PM Agent (Orquestador)                 │
│              projects.json = fuente de verdad             │
├─────────┬──────────┬────────┬───────────┬────────┬───────┤
│Discovery│Propuesta │  QA    │Tech Review│Soporte │Finance│
│  Agent  │  Agent   │ Agent  │  Agent    │ Agent  │ Agent │
├─────────┴──────────┴────────┴───────────┴────────┴───────┤
│                    Onboarding Agent                       │
└──────────────────────────────────────────────────────────┘
     │              │              │              │
┌────┴────┐    ┌────┴────┐   ┌────┴────┐   ┌─────┴─────┐
│WhatsApp │    │ GitHub  │   │ Billing │   │ Client    │
│  API    │    │  API    │   │  APIs   │   │ Systems   │
└─────────┘    └─────────┘   └─────────┘   └───────────┘
```

**Shared State:** `projects.json` + `agents/event-log.jsonl`
**Canal humano:** WhatsApp (alertas) + Dashboard (estado general)

---

## Archivos

```
agents/
├── README.md              ← Este archivo
├── event-log.jsonl        ← Log de eventos (append-only)
├── shared/
│   └── utils.md           ← Convenciones compartidas
├── pm/
│   └── SKILL.md           ← PM Agent
├── propuesta/
│   └── SKILL.md           ← Propuesta Agent
├── qa/
│   └── SKILL.md           ← QA Agent
├── tech-review/
│   └── SKILL.md           ← Tech Review Agent
├── discovery/
│   └── SKILL.md           ← Discovery Agent
├── soporte/
│   └── SKILL.md           ← Soporte Agent
├── onboarding/
│   └── SKILL.md           ← Onboarding Agent
└── finance/
    └── SKILL.md           ← Finance Agent
```

# DOCEPROJECTS — Business Playbook
### Fuente: Conversación estratégica Clara + Emiliano
### Última actualización: 2026-03-04

---

## 1. VISIÓN GENERAL

DOCEPROJECTS es una consultora de automatización e inteligencia artificial dirigida a líderes empresariales colombianos (50+). El modelo opera bajo el concepto **"12:12"** — velocidad, precisión y urgencia como diferenciadores.

**Propuesta de valor central:** No vendemos una solución estática. Vendemos la responsabilidad continua de mantener al cliente en la mejor tecnología disponible. *"We are the surfers."*

---

## 2. CLIENT JOURNEY — MAPA COMPLETO

### FASE 0: Primer Contacto
| Elemento | Detalle |
|----------|---------|
| Canal | WhatsApp (agente AI) |
| Acción | Enviar formulario de diagnóstico tech stack |
| Preguntas | CRM, ERP, plataformas, herramientas actuales |
| Obligatoriedad | No obligatorio — "respondan los que quieran, pero son importantes para los pasos siguientes" |
| Propósito | Radiografía previa para llegar a Discovery con tareas pre-resueltas |
| Sin tech stack | Si el cliente no usa nada digital, es el mejor escenario — describir procesos manuales (cuadernos, libros, etc.) y partir desde cero |

### FASE 1: NDA
| Elemento | Detalle |
|----------|---------|
| Cuándo | Antes del Discovery Call |
| Formato | Se envía previamente o se firma en la reunión |
| Enfoque | Protección bilateral — "nos protege a los dos" |
| Regla | DOCEPROJECTS lo firma primero como gesto de confianza |

### FASE 2: Discovery Call
| Elemento | Detalle |
|----------|---------|
| Grabación | Siempre se graba |
| Estructura | Operación → Pain Points → Oportunidades |
| Enfoque | "Hábleme de operación, no de financiera" |
| Dinámica | Escuchar → Preguntar → Identificar automatizaciones |
| Output | Lista numerada de oportunidades de automatización |
| Cierre | Solicitar datos/APIs necesarios — "Ya tienes el NDA. Yo no voy a frenar." |
| Timer | Al final de la reunión se abre el HTML con cuenta regresiva hacia las 12:12 |
| Duración | Sin límite de tiempo — típicamente 1-3 horas. No hay tope, pero el Discovery debe concluir con suficiente tiempo para producir la propuesta antes del siguiente 12:12 |
| Quién lo conduce | Emiliano o Clara — debe existir una guía/mapa de ruta para que cualquiera de los dos pueda conducirlo de forma consistente |
| Guía Discovery | 🔨 **Pendiente crear:** Ruta crítica con preguntas guía, estructura de conversación, checklist de información a obtener |

#### Política de No-Fit
Si durante el Discovery se identifica que el cliente no es buen fit (no tiene presupuesto, no tiene disposición al cambio, no hay APIs disponibles):
- **Estrategia:** Se envía la propuesta al doble del precio real
- Si el cliente acepta → se ejecuta (hay margen suficiente)
- Si el cliente rechaza → se auto-filtra elegantemente
- Si es realmente imposible técnicamente → conversación honesta y cierre elegante

### FASE 3: Propuesta Comercial (12:12)
| Elemento | Detalle |
|----------|---------|
| Formato | HTML brandeado, responsive en todos los devices |
| Envío | Al siguiente **12:12 en el reloj** (PM o AM) después de que termina el Discovery |
| Timer | Cuenta regresiva visible hasta el siguiente 12:12 — genera urgencia |
| Vigencia | Desde el envío hasta el siguiente 12:12 (12 horas) para aceptar al precio original |
| Contenido | Soluciones propuestas + Preview/Proof of concept de UNA solución |
| Cronograma | En horas/días/semanas — NO en fechas (depende de fecha de aceptación) |
| Estructura | Dividido por clusters de soluciones |
| **Deployment** | **OBLIGATORIO:** Toda propuesta se deploya en `prop.doceprojects.com/<slug>/` encriptada con StatiCrypt. Password: `doce-<slug>`. Ejecutar: `./deploy.sh <slug> <archivo.html>` |

#### Regla de Deployment de Propuestas (OBLIGATORIO)

**Toda propuesta comercial DEBE deployarse siguiendo este estándar, sin excepción:**

| Paso | Detalle |
|------|---------|
| 1. Crear HTML | Propuesta en HTML brandeado usando `proposal-template.html` |
| 2. Deploy al hub | Ejecutar `./deploy.sh <slug> <propuesta.html>` en el repo `mclaramartinez.github.io` |
| 3. URL estándar | `https://prop.doceprojects.com/<slug>/` |
| 4. Password estándar | `doce-<slug>` (se puede personalizar como tercer argumento de deploy.sh) |
| 5. Registrar en projects.json | Agregar campo `proposal` con `url`, `password` y `slug` al proyecto |
| 6. Verificar en dashboard | El link y la contraseña deben aparecer en la card del proyecto en el dashboard |

**Esto aplica para TODOS:** Clara, Emiliano, David, Santiago. No importa quién cree la propuesta.

#### Regla del 12:12 — Cómo Funciona el Timing
| Momento | Qué pasa |
|---------|----------|
| Discovery termina | El reloj empieza — DOCEPROJECTS tiene hasta el **siguiente 12:12** (AM o PM) para enviar la propuesta |
| 12:12 llega | La propuesta se envía automáticamente. Timer del cliente comienza |
| Siguiente 12:12 | Vence la vigencia del precio original. El cliente tuvo 12 horas |
| Después del vencimiento | **Incremento del 12%** sobre el valor de implementación |

**Ejemplo:** Discovery termina a las 3:00 PM → propuesta se envía a las **12:12 AM** (esa misma noche). Cliente tiene hasta las **12:12 PM** del día siguiente para aceptar al precio original.

#### Flexibilidad del Timer
| Escenario | Acción |
|-----------|--------|
| Acepta dentro de la ventana 12:12 | Precio original |
| No acepta en la ventana | **+12%** (negociable pero el principio se mantiene) |
| Cliente necesita más tiempo (consultar socio, etc.) | Flexible — se puede conversar |
| Cliente quiere modificar la oferta | Se modifica, se envía nueva propuesta, timer reinicia al siguiente 12:12 |

**Ejemplos de Preview por tipo de cliente:**
- Dashboard de resumen operativo
- Cotizador de eventos
- Reporte de tendencias de industria

### FASE 3.5: Aceptación → Contrato
| Paso | Acción |
|------|--------|
| 1 | Cliente hace clic en **"Acepto"** en la propuesta HTML |
| 2 | WhatsApp notification automática a Emiliano |
| 3 | Emiliano envía contrato de servicios (PDF o firma digital) |
| 4 | Cliente firma contrato + primer pago |
| 5 | Comienza Fase 4 (Implementación) |

> Si la aceptación ocurre después de la ventana 12:12 → el contrato refleja el 12% de incremento.

### FASE 4: Implementación (por Clusters de Soluciones)
| Elemento | Detalle |
|----------|---------|
| Lógica de fases | Agrupadas por **clusters funcionales** — soluciones que comparten integraciones, APIs o fuentes de datos se construyen y entregan juntas |
| Previews | Cada cluster incluye un preview antes de la entrega final |
| Customer Journey | "Les voy entregando de a poquito pero todavía no está, miren cómo está quedando" |
| Pipeline | Lógica interna de cuadrar disponibilidad y orden de proyectos |

#### Framework Estándar de Clusters

| Fase | Lógica | Entregable |
|------|--------|-----------|
| **Cluster A** | Soluciones que tocan los mismos sistemas/datos. Se priorizan las de mayor impacto operativo | Primer grupo de soluciones en producción + Cangrejo activo sobre ellas |
| **Cluster B** | Siguiente grupo de soluciones relacionadas entre sí | Segundo grupo en producción |
| **Cluster C + Handoff** | Soluciones restantes + entrenamiento + setup grupo WhatsApp + status page | Todo en producción, post-venta comienza |

**Principio:** No entregar por etapa de trabajo (diseño→desarrollo→testing). Entregar por clusters funcionales que el cliente puede **usar inmediatamente** al recibirlos.

**Ejemplo:** Si el cliente tiene un cotizador y un dashboard que usan la misma base de datos de productos → van en el mismo cluster. Un agente de WhatsApp que es independiente → cluster separado.

### FASE 5: Post-Venta
| Elemento | Detalle |
|----------|---------|
| Grupo WhatsApp | Con dolientes/stakeholders del proceso automatizado |
| Bot Customer Service | Agente dedicado por cliente para soporte |
| Status Page | Disponible 24/7 para el cliente |
| Reporte Semanal | Resumen automático del estado de todas las soluciones (informativo, no decisorio — lleva disclaimer) |
| Incidentes | Se trippean automáticamente si algo falla |

### FASE 6: Mantenimiento Continuo
| Elemento | Detalle |
|----------|---------|
| Cobertura | Infraestructura física + solución de software |
| Monitoreo | El "Cangrejo" testea constantemente todas las soluciones |
| Upgrade | Obligación de migrar a mejor tecnología cuando aparezca |
| Precio | Fee mensual fijo |

---

## 3. MODELO DE REVENUE

### Estructura de Cobro
| Concepto | Detalle |
|----------|---------|
| **Implementación** | Fee único por proyecto/cluster |
| **Mantenimiento mensual** | Fee mensual fijo por cliente |

### Lógica de Pricing
- Fee de implementación se define en la propuesta comercial, basado en complejidad y cantidad de soluciones
- Fee de mantenimiento es fijo y mensual — cubre monitoreo, soporte, upgrades, Cangrejo, regalos
- **Cash vs Digital:** No hay diferenciación de precio

### Regalos Post-Venta (El cliente escoge 1 de 3)
| # | Regalo | Descripción |
|---|--------|-------------|
| 1 | **Bancolombia SMS Tracker** | Shortcut de iPhone que organiza los SMS transaccionales de Bancolombia en un resumen financiero |
| 2 | **Reportero de Industria** | Agente que entrega semanalmente las noticias más relevantes de la industria del cliente |
| 3 | **Suite de Productividad** | Agente que gestiona correo y calendario (Google/Outlook) — resúmenes, priorización |

**Regla:** Los regalos son personales, no del negocio. Valor individual ~1M COP. "Estás creyendo en mí, te regalo uno."

**Costo operativo de regalos:** Incluido en el fee de mantenimiento mensual. El Reportero de Industria y la Suite consumen API calls de forma continua — el mantenimiento mensual debe cubrir este costo.

---

## 4. SCOPE CREEP — REGLA CLARA

### ¿Qué es soporte incluido vs. nuevo desarrollo?

| Categoría | Definición | Se cobra? |
|-----------|-----------|-----------|
| **Soporte / Mantenimiento** | Actualización, corrección o mejora de un proceso **ya implementado** | ❌ Incluido en mantenimiento |
| **Error de DOCEPROJECTS** | El proceso no quedó bien porque no se entendió correctamente en el Discovery | ❌ Se corrige sin costo — siempre es culpa nuestra |
| **Nuevo desarrollo** | El cliente pide automatizar un **proceso diferente** al que se contrató | ✅ Se cotiza como nuevo proyecto |

### Regla de oro
> Si el proceso es el mismo que se contrató → es mantenimiento, sin importar cuántas mejoras requiera.
> Si el proceso es diferente → es nuevo desarrollo, se cotiza aparte.

**Ejemplo:** El cliente contrató un agente de customer service. Luego quiere que ese agente escale a un agente técnico separado → **nuevo desarrollo** (proceso diferente). Pero si el agente de customer service necesita responder mejor o cubrir más casos dentro del mismo proceso → **mantenimiento incluido**.

---

## 5. SISTEMA INTERNO — "EL CANGREJO" 🦀

El **Cangrejo** es el sistema interno de testing y monitoreo automatizado de DOCEPROJECTS.

### Funciones del Cangrejo
| Función | Detalle |
|---------|---------|
| **Testing continuo** | Testea agentes, funcionamiento, botones, flujos |
| **Testing con datos reales** | Testea en producción con datos reales del cliente, no con datos sintéticos |
| **Creación de escenarios** | Crea agentes de testing con 50+ formas de equivocarse |
| **Dashboard interno** | Reporta resultados en dashboard privado de DOCEPROJECTS |
| **Seguimiento de cotizaciones** | Hace follow-up de cotizaciones enviadas |
| **Envío programado** | Envía cotizaciones a las 12:12 |
| **Evaluación tecnológica** | Revisa si la solución sigue siendo la mejor disponible |

### Cangrejo → Cliente
- Status page pública por cliente
- Reporte semanal automático
- Trigereo de incidentes automático
- Mensaje periódico: "Tus soluciones siguen corriendo al 100%"

---

## 6. RESILIENCIA TECNOLÓGICA

### API Fallback (Multi-Modelo) — Estrategia por Fases

El multi-modelo es esencial pero no se lanza todo a la vez. Rollout por fases:

| Fase | Cuándo | Alcance |
|------|--------|---------|
| **v1 — Lanzamiento** | Día 1 | Claude (Anthropic) únicamente. Enviar rápido, entregar valor |
| **v2 — Mes 3+** | Después de estabilizar primeros clientes | Agregar GPT como fallback para soluciones críticas. Construir herramienta adaptadora de prompts |
| **v3 — Mes 6+** | Operación madura | Multi-modelo completo (Claude + GPT + Gemini). Cangrejo testea los 3 modelos |

**Regla:** Cada solución que use LLMs debe tener **prompts dedicados por modelo** (no se reutilizan). Un prompt de Claude no funciona igual en GPT o Gemini. Se construye un **creador de prompts** interno que adapte automáticamente los prompts para cada proveedor.

### Infraestructura Física
| Necesidad | Solución |
|-----------|----------|
| Energía | Generador automático (tipo Red Valley) |
| Internet | VPN gringa como respaldo / Starlink |
| Hosting | Cloud — evaluar ubicación (Colombia vs. USA) |

### Obligación de Upgrade
- **Regla de oro:** Si aparece mejor tecnología, DOCEPROJECTS tiene la obligación de rehacer la solución y entregarla actualizada.
- No se cobra el upgrade al cliente — **siempre absorbido por el mantenimiento**.
- El lenguaje base siempre será **Python**. Si el cliente requiere otra tecnología, no es lo que DOCEPROJECTS hace.
- Si el upgrade requiere más hardware o más capacidad de cómputo → **el cliente paga el hardware/infraestructura**, DOCEPROJECTS absorbe el esfuerzo de desarrollo.
- Si el upgrade requiere más tokens/API calls → **el cliente paga el consumo incremental**.

---

## 7. SLA Y SOPORTE 24/7

### Estructura de Soporte
| Nivel | Quién | Función |
|-------|-------|---------|
| **Nivel 1** | Agente AI de customer service | Filtrar lo real de lo no real. Intentar resolver en primera instancia. Entender el problema si no puede resolverlo |
| **Nivel 2** | Clara o Emiliano | Problemas reales que el agente no pudo resolver. Llega con contexto del Nivel 1 |
| **Nivel 3** | Ambos | Incidentes críticos — "quema el celular" |

### Reglas de SLA
- El agente de Nivel 1 es **obligatorio** antes de escalar — filtra ruido
- Si es un incidente real → notificación inmediata a ambos, sin importar la hora
- Cualquiera de los dos debe ser capaz de tomar el problema y resolverlo
- **Pendiente definir:** Porcentaje de uptime garantizado (¿99.9%?), tiempos de respuesta por nivel

---

## 8. LEGAL Y PROTECCIÓN

### Contrato de Servicios
| Elemento | Decisión |
|----------|----------|
| Tipo de documento | Contrato privado como personas naturales (no pagaré, no empresa) |
| Contenido mínimo | Entregables, timeline, términos de pago, IP, terminación, garantías |
| NDA | Documento separado, ya definido |
| 🔨 **Pendiente** | Definir formato exacto — buscar asesoría legal para contrato entre personas naturales |

### Propiedad Intelectual (IP)
| Aspecto | Regla |
|---------|-------|
| Código adaptado al cliente | El cliente es dueño de una **instancia desplegada y funcionando** — no del código fuente |
| Código fuente / repos | **DOCEPROJECTS retiene** el código fuente, repos, y derecho a reutilizar |
| Replicación | DOCEPROJECTS puede usar la misma solución base para otros clientes |
| Transparencia | El cliente no necesita saber que la solución se replica — pero tampoco se oculta si pregunta |

### Exit Policy — Cuando un Cliente se Va
| Paso | Acción |
|------|--------|
| 1 | Se entrega el **computador físico** con las soluciones corriendo y datos guardados |
| 2 | **NO se entregan los repos** ni el código fuente — ese es el valor de DOCEPROJECTS |
| 3 | Los datos del cliente se entregan completos |
| 4 | Si no tiene computador propio → se entregan los datos, se apaga todo |
| 5 | No hay periodo de transición definido — se cierra limpiamente |

> **El valor de DOCEPROJECTS está en los repos y el conocimiento.** El cliente recibe su máquina funcionando, pero no el código fuente.

### Responsabilidad por Errores de AI
| Regla | Detalle |
|-------|---------|
| **Responsabilidad** | Del cliente. DOCEPROJECTS no se hace responsable de errores de AI |
| **En el contrato** | Cláusula explícita de descargo de responsabilidad |
| **En la solución** | Disclaimer visible permanente: "Revise antes de usar" |
| **Recordatorios** | Mensajes periódicos al cliente: "Recuerde que usted debe estar revisando" |
| **Correcciones** | DOCEPROJECTS está abierto a corregir las veces que sea necesario |
| **Principio** | Igual que Claude/ChatGPT dicen "puedo cometer errores" — las soluciones de DOCEPROJECTS llevan el mismo disclaimer |

---

## 9. PERFIL DE CLIENTE IDEAL (ICP)

### Requisito Principal
> El cliente debe **identificar la oportunidad** de optimizar o automatizar sus procesos. No puede ser alguien que piense que lo suyo es perfecto tal como está.

### Criterios Secundarios
| Factor | Relevancia |
|--------|-----------|
| Edad | No relevante |
| Industria | No relevante — cualquier sector |
| Tamaño | Relevante — lo suficientemente grande para no poder hacer la solución in-house, pero no tan grande que tenga equipo técnico propio |
| Ubicación | Colombia (inicialmente) |
| Nivel digital | No relevante — desde "no tiene nada" (el mejor caso) hasta "usa Excel y WhatsApp" |
| Disposición | Debe reconocer que sus procesos se pueden mejorar |

---

## 10. ESTRATEGIA DE CRECIMIENTO

### Adquisición de Clientes
| Canal | Estrategia |
|-------|-----------|
| **Referidos** | Canal principal. Programa de referrals agresivo (ver abajo) |
| **Eventos** | Presencia en eventos empresariales, networking |
| **LinkedIn** | 🔨 Pendiente definir estrategia |
| **Cold Outreach** | 🔨 Pendiente definir |

### Programa de Referrals
| Incentivo | Detalle |
|-----------|---------|
| Cliente que refiere | Reducción en su mantenimiento mensual |
| Ejemplo | Primeros 6 meses a ~1.5 salarios mínimos |
| Filosofía | Lo que se invertiría en pauta publicitaria → se invierte en descuentos de referral |

> Necesita un programa de referrals **muy sólido**. Es la estrategia de adquisición principal.

### Diferenciadores vs. Competencia
| Factor | Ventaja DOCEPROJECTS |
|--------|---------------------|
| Velocidad | Propuesta antes del siguiente 12:12 con preview funcional |
| Eficiencia | Comprensión rápida del negocio |
| Hosting físico | Computador dedicado del cliente — modelo único |
| Costo | Probablemente más competitivo que agencias tradicionales |
| Mantenimiento continuo | No es "construir y abandonar" — relación continua |

### Plan de Contratación
| Orden | Rol | Por qué |
|-------|-----|---------|
| 1º | **Implementador** | Lo más difícil y lo que determina el éxito o fracaso |
| 2º | **Persona de seguridad/técnica** | Surveillance técnico y seguridad de las soluciones |
| 3º+ | Más desarrolladores + más comerciales | Crecimiento proporcional |

**Estructura base:** Emiliano (vendedor/comercial) + Clara (desarrolladora/técnica). Crecimiento en ambos ejes.

---

## 11. ORGANIZACIÓN INTERNA

### División de Roles (Actual)
| Persona | Enfoque principal |
|---------|------------------|
| **Emiliano** | Reuniones, ventas, relación con clientes, Discovery Calls |
| **Clara** | Desarrollo, implementación técnica, infraestructura |

> Ambos deben poder conducir un Discovery Call usando la guía estandarizada.

### Dashboard de Proyectos
- Organizado por **tipo de solución**, NO por cliente
- Permite reutilización y replicación eficiente
- Cada solución se construye una vez, se replica N veces
- 🔨 **Pendiente:** Definir estructura de repos — monorepo vs. repo por tipo de solución. Definir cómo manejar customizaciones por cliente sin romper la base compartida

### Herramientas Cloud
- Todas las herramientas internas viven en cloud
- Cada herramienta incluye:
  - Reglas de branding incorporadas
  - Templates de cotización pre-configurados
  - Lógica de propuesta consistente

### C-Suite de AI
- Agentes internos que funcionan como asesores:
  - Seguridad
  - Tecnología
  - Operaciones
- Construidos con Claude Code
- Son la capa de inteligencia sobre el Cangrejo

### Capacidad Operativa
| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántos clientes simultáneos? | No definido — se irá viendo a medida que crezcan |
| ¿Dos Discoveries el mismo día? | Se sacan las dos, sin excepción |
| ¿Pipeline management? | No definido aún — se priorizará a medida que entre flujo |

---

## 12. UNIT ECONOMICS — MODELO POR CLIENTE

### Revenue por Cliente
| Concepto | Valor | Frecuencia |
|----------|-------|-----------|
| Fee de implementación | $_______ COP | Único (por cluster) |
| Fee de mantenimiento | $_______ COP | Mensual |
| Total año 1 | Implementación + (Mantenimiento × 12) | — |

### Costo por Cliente
| Concepto | Costo estimado/mes | Notas |
|----------|-------------------|-------|
| API calls (LLMs) | $_______ | Claude + backups cuando se activen |
| Hosting / compute | $_______ | Cloud + compute del Cangrejo |
| Cangrejo (testing continuo) | $_______ | Incluido en infraestructura |
| Soporte (tiempo humano) | $_______ | Horas/mes promedio post-estabilización |
| Regalos (API calls continuos) | $_______ | Reportero de Industria / Suite de Productividad |
| **Total costo/mes** | $_______ | — |

### Margen
| Métrica | Fórmula |
|---------|---------|
| Margen bruto/mes | Mantenimiento - Costo total/mes |
| Punto de no-rentabilidad | Si margen < 0 → revisar fee o costo |
| Payback | ¿Cuántos meses de mantenimiento cubren el costo de implementación? |

### Breakeven Operativo
| Variable | Valor |
|----------|-------|
| Costos fijos mensuales (infra, tools, tiempo) | $_______ COP |
| Clientes en mantenimiento necesarios para cubrir fijos | _______ |

> **Pendiente:** Emiliano llena los valores. Una vez completos, este modelo determina si el pricing es viable.

---

## 13. MATRIZ DE RIESGOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|-----------|
| Aumento de precio API Claude | Media | Alto | Fallback multi-modelo ya planeado (v2-v3) |
| Persona clave no disponible (somos 2) | Alta | Crítico | Guía de Discovery documentada + procesos replicables |
| Concentración de clientes | Alta (etapa temprana) | Alto | Programa de referrals para diversificar base |
| Scope creep a pesar de reglas | Media | Medio | Contrato claro + proceso de cambio de alcance |
| Multi-modelo inviable al lanzamiento | Media | Alto | Estrategia por fases: Claude-first, backups después |
| Competidor copia modelo 12:12 | Baja | Medio | La velocidad de ejecución es el moat, no el concepto |
| Error de AI le cuesta al cliente | Media | Alto | Disclaimer contractual + recordatorios + correcciones ilimitadas |
| Cliente se va y replica internamente | Baja | Medio | Repos no se entregan — solo instancia funcionando |

---

## 14. KPIs — MÉTRICAS DE ÉXITO

| KPI | Target | Frecuencia | Cómo se mide |
|-----|--------|-----------|-------------|
| Time-to-proposal | Antes del siguiente 12:12 | Per deal | Timestamp Discovery end → Timestamp envío |
| Proposal win rate | Trackear (sin target aún) | Mensual | Propuestas aceptadas / propuestas enviadas |
| Clientes en mantenimiento activo | Crecimiento mes a mes | Mensual | Conteo |
| Tasa de retención | >90% | Trimestral | Clientes renovados / clientes totales |
| Referral conversion | Trackear | Mensual | Referidos que firman / referidos totales |
| Cangrejo uptime | 99%+ | Semanal | Status page |
| Valor promedio de contrato (ACV) | Trackear | Mensual | Revenue total / # contratos |
| Tickets de soporte/cliente | Trackear (menor = mejor) | Mensual | Tickets N1 por cliente |
| Tiempo medio de resolución | Trackear | Mensual | MTTR desde ticket → resolución |

---

## 15. SALES FUNNEL & CAPACITY

### Pipeline Completo
```
Leads (referrals/eventos) → Discovery Calls → Propuestas 12:12 → Firmados → Implementados → Mantenimiento
```

### Conversion Tracking
| Etapa | Métrica | Target |
|-------|---------|--------|
| Lead → Discovery | % de leads que agendan | Trackear |
| Discovery → Propuesta | % que reciben propuesta (debería ser ~100%) | 100% |
| Propuesta → Firma | Win rate | Trackear |
| Firma → Implementación exitosa | Completion rate | 100% |
| Implementación → Mantenimiento | Renewal rate | >90% |

### Capacidad con 2 Personas
| Restricción | Estimado |
|-------------|----------|
| Discovery Calls / semana | 3-4 máximo |
| Implementaciones concurrentes | 2-3 máximo |
| Propuestas / semana | 3-4 (ligado a Discoveries) |
| Revenue ceiling (antes de contratar) | (Discovery/semana × win rate × ACV) — calcular |

### Cuándo Contratar
| Signal | Acción |
|--------|--------|
| Discovery calls se empiezan a rechazar por falta de tiempo | Contratar implementador (1er hire) |
| Post-venta consume >50% del tiempo | Contratar persona técnica (2do hire) |
| Pipeline tiene >5 leads calientes esperando | Evaluar capacidad comercial |

---

## 16. REGLAS DE NEGOCIO CLAVE

| # | Regla | Detalle |
|---|-------|---------|
| 1 | **Todo 12:12** | Propuestas se envían al siguiente 12:12 en el reloj. Cliente tiene hasta el siguiente 12:12 para aceptar |
| 2 | **12% por demora** | Si el cliente no acepta en la ventana 12:12, incremento del 12% en implementación (negociable) |
| 3 | **NDA primero** | Siempre antes del Discovery, DOCEPROJECTS firma primero |
| 4 | **Siempre grabar** | Todo Discovery Call se graba |
| 5 | **Operación primero** | Discovery enfocado en operación, no en finanzas |
| 6 | **Sin límite de tiempo en Discovery** | Típicamente 1-3h. Sin tope, pero debe concluir antes del siguiente 12:12 |
| 7 | **Preview obligatorio** | Toda propuesta incluye un proof-of-concept funcional |
| 8 | **Clusters, no bloques** | Entregas por clusters funcionales de soluciones con previews intermedios |
| 9 | **Cronograma relativo** | Horas/días/semanas, nunca fechas fijas |
| 10 | **Upgrade obligatorio** | Si hay mejor tecnología, se rehace sin costo adicional |
| 11 | **Mismo proceso = mantenimiento** | Mejoras al mismo proceso no se cobran. Proceso nuevo = nueva cotización |
| 12 | **Error nuestro = gratis** | Si no entendimos el proceso en Discovery, la corrección va por nuestra cuenta |
| 13 | **AI disclaimer siempre** | Toda solución lleva disclaimer de que puede cometer errores — el cliente revisa |
| 14 | **Repos no se entregan** | El cliente recibe su instancia funcionando, nunca el código fuente |
| 15 | **Prompts por modelo** | Cada solución tiene prompts dedicados por LLM — desplegado por fases (v1: Claude, v2: +GPT, v3: +Gemini) |
| 16 | **Referrals > Pauta** | Invertir en programa de referidos, no en publicidad |
| 17 | **Solución > Cliente** | Organización interna por solución, no por cliente |
| 18 | **Branding integrado** | Toda herramienta interna tiene las reglas de marca incorporadas |
| 19 | **Incógnito** | Operación discreta — regla en NDA |
| 20 | **Propuesta = Hub** | Toda propuesta se deploya en `prop.doceprojects.com/<slug>/` con StatiCrypt. Password `doce-<slug>`. Registrar URL + password en `projects.json` + dashboard. Sin excepción |

---

## 17. ACTION ITEMS — PRIORIZADOS

### 🔴 Prioridad ALTA (Necesarios para operar)

| # | Acción | Responsable | Estado |
|---|--------|-------------|--------|
| 1 | Diseñar y desarrollar el template HTML de propuesta comercial | Clara | ✅ Completado |
| 2 | Crear el formulario de diagnóstico tech stack para WhatsApp agent | Clara | 🔨 En progreso |
| 3 | Diseñar template de NDA bilateral | Clara + Emiliano | ⏳ Pendiente |
| 4 | **Crear guía/mapa de ruta del Discovery Call** — ruta crítica, preguntas guía, checklist | Clara + Emiliano | ⏳ Pendiente |
| 5 | **Crear contrato de servicios** (persona natural) — entregables, pagos, IP, terminación, disclaimer AI | Clara + Emiliano + Legal | ⏳ Pendiente |
| 6 | Construir el sistema de envío programado a las 12:12 | Clara | ⏳ Pendiente |
| 7 | Definir y documentar los clusters estándar de entrega | Clara + Emiliano | ⏳ Pendiente |
| 8 | Setup de infraestructura cloud (hosting, backups) | Clara | ⏳ Pendiente |
| 9 | **Llenar unit economics** — valores reales de pricing e costs | Emiliano | ⏳ Pendiente |

### 🟡 Prioridad MEDIA (Necesarios para escalar)

| # | Acción | Responsable | Estado |
|---|--------|-------------|--------|
| 10 | Construir el Cangrejo v1 — testing automatizado con datos reales | Clara | ⏳ Pendiente |
| 11 | Crear dashboard interno organizado por tipo de solución | Clara | ⏳ Pendiente |
| 12 | **Construir creador de prompts** que adapte automáticamente a Claude/GPT/Gemini | Clara | ⏳ Pendiente |
| 13 | Implementar API fallback multi-modelo con prompts dedicados (v2) | Clara | ⏳ Pendiente |
| 14 | **Construir agente de customer service Nivel 1** (filtro + primera resolución) | Clara | ⏳ Pendiente |
| 15 | Diseñar status page template para clientes | Clara | ⏳ Pendiente |
| 16 | Crear bot de customer service template (replicable por cliente) | Clara | ⏳ Pendiente |
| 17 | Definir estructura de reporte semanal automatizado | Clara + Emiliano | ⏳ Pendiente |
| 18 | **Diseñar programa de referrals** — incentivos, mecánica, descuentos | Emiliano | ⏳ Pendiente |
| 19 | **Definir estructura de repos** — monorepo vs. repo por solución, manejo de customizaciones | Clara | ⏳ Pendiente |

### 🟢 Prioridad BAJA (Nice to have / Post-lanzamiento)

| # | Acción | Responsable | Estado |
|---|--------|-------------|--------|
| 20 | Desarrollar regalo #1: Bancolombia SMS Shortcut (iPhone) | Clara | ⏳ Pendiente |
| 21 | Desarrollar regalo #2: Reportero de Industria (agente de noticias) | Clara | ⏳ Pendiente |
| 22 | Desarrollar regalo #3: Suite de Productividad (correo/calendario) | Clara | ⏳ Pendiente |
| 23 | Construir C-Suite de agentes AI internos (seguridad, tech, ops) | Clara | ⏳ Pendiente |
| 24 | Evaluar ubicación de infraestructura (Colombia vs USA) | Clara + Emiliano | ⏳ Pendiente |
| 25 | Investigar backup de internet (VPN/Starlink) | Clara | ⏳ Pendiente |
| 26 | Investigar backup de energía (generador) | Emiliano | ⏳ Pendiente |

---

## 18. CONEXIÓN CON BRAND MANUAL

El Brand Manual de DOCEPROJECTS (`brand-manual.html`) ya incluye los fundamentos visuales. Aquí se documenta cómo cada pieza del playbook se conecta con la marca:

| Elemento de Negocio | Componente de Marca | Estado |
|---------------------|---------------------|--------|
| Template de propuesta HTML | Colores, tipografía, logo, Product UI System | ✅ Completado |
| Formulario WhatsApp | Tono de voz, colores de UI | ✅ Definido en Brand Voice |
| NDA | Logo, tipografía formal (Inter) | 🔨 Por construir |
| Contrato de servicios | Logo, tipografía formal | 🔨 Por construir |
| Status Page | Dashboard Layout Logic, Dark Mode Rules | ✅ Definido en Product UI |
| Reporte Semanal | Color system, data tables, card specs | ✅ Definido en Product UI |
| Regalos (3 opciones) | Brand Architecture, naming rules | ✅ Definido en Brand Architecture |
| Cotización (countdown) | Purple accent, Bebas Neue headlines, motion principles | ✅ Definido en Brand Manual |
| Dashboard interno | Navy dark theme, component system | ✅ Definido en Product UI |

---

## 19. DECISIONES PENDIENTES

> Las siguientes preguntas quedaron abiertas. Una vez resueltas, se integran al playbook.

| # | Pregunta | Estado |
|---|----------|--------|
| 1 | **Estructura de repos** — ¿Monorepo, repo por solución, cómo manejar customizaciones? | ⏳ Pendiente |
| 2 | **SLA numérico** — ¿99.9% uptime? ¿Tiempos de respuesta por nivel? | ⏳ Pendiente |
| 3 | **Formato legal del contrato** — ¿Cómo se estructura un contrato entre personas naturales? Necesita asesoría legal | ⏳ Pendiente |
| 4 | **Estrategia de adquisición digital** — LinkedIn, cold outreach, contenido | ⏳ Pendiente |

---

*Este documento es la fuente de verdad para la metodología y el journey de DOCEPROJECTS. Se mantiene sincronizado con el Brand Manual y sirve como guía para la generación de propuestas consistentes.*

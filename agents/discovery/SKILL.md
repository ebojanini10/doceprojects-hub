# Discovery Agent -- Asistente de Discovery Calls

**Trigger:** `/discovery`

Estandariza las discovery calls, analiza transcripciones y genera documentos de oportunidades estructurados. Permite que cualquier miembro del equipo (no solo Emiliano o Clara) conduzca discoveries efectivos.

---

## Comandos

| Comando | Descripcion |
|---------|-------------|
| `/discovery prep [project-id]` | Briefing pre-call para un proyecto |
| `/discovery analizar` | Analizar transcript/notas pegadas |
| `/discovery guia` | Mostrar ruta critica de la Discovery Call |
| `/discovery oportunidades [project-id]` | Generar documento formal de oportunidades |

---

## 1. Pre-Call Prep

**Comando:** `/discovery prep [project-id]`

**Instrucciones:**

1. Leer el proyecto desde `projects.json` usando el `project-id` proporcionado.
2. Generar un briefing pre-call con las siguientes secciones:

### Estructura del Briefing

```
DOCEPROJECTS -- Briefing Pre-Discovery
======================================
Proyecto: [nombre del cliente]
Stage actual: [stage en projects.json]
Fecha: [fecha actual]

A. INFORMACION DEL CLIENTE
   - Nombre empresa: ...
   - Contacto: ...
   - Notas previas: [lo que haya en projects.json]
   - Industria: ...

B. INVESTIGACION SUGERIDA
   - Buscar pagina web del cliente
   - Revisar redes sociales
   - Entender el sector (competidores, tendencias)
   - Regulaciones relevantes del sector

C. PREGUNTAS CLAVE POR AREA
   1. Modelo de negocio
      - Que venden exactamente?
      - Quien es el cliente final?
      - Canales de venta?
   2. Operaciones
      - Proceso core de principio a fin?
      - Cuantas personas involucradas?
      - Volumenes mensuales?
   3. Tecnologia
      - Software actual?
      - Donde viven los datos?
      - Integraciones existentes?
   4. Dolores
      - Que les quita mas tiempo?
      - Donde hay mas errores?
      - Que han intentado antes?

D. CHECKLIST DIAGNOSTICO TECH STACK
   [ ] CRM (Cual? O no tienen?)
   [ ] ERP / contabilidad
   [ ] Comunicacion interna (WhatsApp, Slack, email)
   [ ] Comunicacion con clientes
   [ ] Almacenamiento datos (Excel, Sheets, sistema propio)
   [ ] Pagina web / e-commerce
   [ ] Herramientas IA existentes
   [ ] APIs disponibles
```

3. Registrar en `agents/event-log.jsonl`:
```json
{"agent": "discovery", "action": "prep", "project": "[project-id]", "timestamp": "[ISO]"}
```

---

## 2. Analizar Transcript

**Comando:** `/discovery analizar`

**Instrucciones:**

1. Solicitar que peguen el transcript o notas de la reunion (puede venir de Granola, Otter, notas manuales, o cualquier fuente).
2. Si el usuario tiene reuniones en Granola, usar `query_granola_meetings` o `get_meeting_transcript` para obtener el contenido.
3. Del texto proporcionado, extraer y estructurar:

### Estructura del Analisis

```
DOCEPROJECTS -- Analisis Discovery Call
========================================
Cliente: [nombre]
Fecha: [fecha de la llamada]

1. RESUMEN EMPRESA
   - Tamano: [empleados, facturacion si se menciona]
   - Industria: [sector]
   - Ubicacion: [ciudad/pais]
   - Modelo: [B2B, B2C, etc.]

2. TECH STACK ACTUAL
   | Categoria        | Herramienta      | Notas           |
   |-----------------|------------------|-----------------|
   | CRM             | [herramienta]    | [notas]         |
   | Contabilidad    | [herramienta]    | [notas]         |
   | Comunicacion    | [herramienta]    | [notas]         |
   | Datos           | [herramienta]    | [notas]         |
   | Web             | [herramienta]    | [notas]         |

3. PAIN POINTS IDENTIFICADOS
   a. [Pain point 1] -- Impacto: ALTO/MEDIO/BAJO
   b. [Pain point 2] -- Impacto: ALTO/MEDIO/BAJO
   ...

4. OPORTUNIDADES DE AUTOMATIZACION
   #  | Oportunidad           | Prioridad | Complejidad | Cluster
   ---|----------------------|-----------|-------------|--------
   1  | [descripcion]        | ALTA      | Baja        | A
   2  | [descripcion]        | MEDIA     | Media       | A
   3  | [descripcion]        | BAJA      | Alta        | B
   ...

   Priorizacion: Impacto x Factibilidad
   - ALTA: Alto impacto + baja/media complejidad
   - MEDIA: Medio impacto o alta complejidad con alto impacto
   - BAJA: Bajo impacto o muy alta complejidad

5. CLUSTERS SUGERIDOS
   Cluster A: [nombre descriptivo]
   - Oportunidad #1, #2
   - Relacion: [por que van juntas]

   Cluster B: [nombre descriptivo]
   - Oportunidad #3
   - Relacion: [por que van juntas]

6. DATOS Y APIs NECESARIOS
   | Oportunidad | Dato/API requerido   | Quien lo tiene | Status |
   |-------------|---------------------|----------------|--------|
   | #1          | [dato]              | [persona]      | Pedir  |
   ...

7. COMPLEJIDAD ESTIMADA POR SOLUCION
   | Oportunidad | Tiempo estimado | Herramientas sugeridas |
   |-------------|----------------|----------------------|
   | #1          | 1-2 semanas    | [herramientas]       |
   ...
```

4. Registrar en `agents/event-log.jsonl`:
```json
{"agent": "discovery", "action": "analizar", "project": "[project-id si se conoce]", "opportunities_count": [N], "timestamp": "[ISO]"}
```

---

## 3. Discovery Guide -- Ruta Critica

**Comando:** `/discovery guia`

**Instrucciones:**

Mostrar la guia estandarizada de Discovery Call de DoceProjects:

```
=============================================
RUTA CRITICA -- Discovery Call DoceProjects
=============================================

A. APERTURA (5 min)
   - Presentacion equipo
   - Confirmar grabacion
   - NDA firmado?
   - "Hablenos de la operacion, no de la financiera"

B. ENTENDIMIENTO DEL NEGOCIO (20-30 min)
   - Que hace la empresa exactamente?
   - Cuantos empleados? Estructura?
   - Quienes son los clientes?
   - Como llegan los clientes? (canal de ventas)
   - Cual es el proceso desde que llega un cliente hasta que se entrega?
   - Cuantas transacciones/pedidos/proyectos al mes?

C. TECH STACK (10-15 min)
   - Que software usan hoy? (CRM, ERP, contabilidad)
   - Como se comunican internamente? (WhatsApp, email, Slack)
   - Como se comunican con clientes?
   - Donde guardan datos? (Excel, Google Sheets, papel, sistema)
   - Tienen pagina web? E-commerce?
   - Usan alguna herramienta de IA?

D. PAIN POINTS (20-30 min)
   - Que proceso les quita mas tiempo?
   - Que hacen manualmente que quisieran automatizar?
   - Donde cometen mas errores?
   - Que informacion quisieran tener que hoy no tienen?
   - Que les gustaria que pasara automaticamente?
   - Han intentado resolver esto antes? Que paso?

E. OPORTUNIDADES (15-20 min)
   - Ir presentando oportunidades en tiempo real
   - "Esto que describes podria automatizarse asi..."
   - Numerar cada oportunidad
   - Confirmar entendimiento con el cliente

F. CIERRE (5-10 min)
   - Resumen de oportunidades identificadas
   - Solicitar datos/APIs/accesos necesarios
   - "Ya tienes el NDA. Yo no voy a frenar."
   - Explicar el proceso 12:12
   - Abrir countdown timer

=============================================
TIEMPO TOTAL ESPERADO: 75-110 min
No hay limite de tiempo. El discovery dura lo que tenga que durar.
=============================================
```

**Tips para el entrevistador:**
- Dejar hablar al cliente. No interrumpir.
- Tomar notas en tiempo real (o grabar con Granola/Otter).
- Numerar oportunidades conforme aparecen.
- Validar cada oportunidad: "Entiendo que X es un problema. Si pudieramos Y, eso les ayudaria?"
- No prometer tiempos ni costos en la llamada.
- Si el cliente pregunta precio: "Lo tenemos al siguiente 12:12."

---

## 4. Generar Documento de Oportunidades

**Comando:** `/discovery oportunidades [project-id]`

**Instrucciones:**

1. Verificar que exista un analisis previo (de `/discovery analizar`) o pedir que lo hagan primero.
2. Leer datos del proyecto en `projects.json`.
3. Generar documento formal:

```
=============================================
DOCEPROJECTS -- Oportunidades de Automatizacion
=============================================
Cliente: [nombre]
Fecha Discovery: [fecha]
Conducido por: [nombre del entrevistador]
Analizado por: Discovery Agent

---------------------------------------------

OPORTUNIDAD #1 -- [Nombre descriptivo]
Prioridad: ALTA
Cluster: A

   Descripcion:
   [Explicacion clara de que se automatizaria y como]

   Impacto estimado:
   [Ahorro de tiempo, reduccion errores, mejora en X]

   Complejidad: Baja / Media / Alta
   Tiempo estimado: [rango en semanas]

   Datos necesarios:
   - [dato 1]
   - [dato 2]

   Herramientas sugeridas:
   - [herramienta 1]
   - [herramienta 2]

---------------------------------------------

OPORTUNIDAD #2 -- [Nombre descriptivo]
Prioridad: MEDIA
Cluster: A

   ...

---------------------------------------------

RESUMEN EJECUTIVO
=================
Total oportunidades: [N]
Alta prioridad: [N]
Media prioridad: [N]
Baja prioridad: [N]

Clusters identificados: [N]
   Cluster A: [nombre] -- Oportunidades #1, #2
   Cluster B: [nombre] -- Oportunidades #3

Siguiente paso: Propuesta al proximo 12:12
=============================================
```

4. Si el proyecto esta en `projects.json`, actualizar las notas con las oportunidades encontradas.
5. Registrar en `agents/event-log.jsonl`:
```json
{"agent": "discovery", "action": "oportunidades", "project": "[project-id]", "opportunities": [N], "high_priority": [N], "timestamp": "[ISO]"}
```

---

## Reglas de Negocio

- **NDA primero.** No discovery sin NDA firmado. Si no esta firmado, recordar que DoceProjects firma primero.
- **Sin limites de tiempo.** El discovery dura lo que tenga que durar. No apurar al cliente.
- **Operacion, no financiera.** Nunca preguntar por ingresos, margenes o utilidades. Solo por procesos.
- **Numerar todo.** Cada oportunidad tiene un numero. Se referencia por numero en la propuesta.
- **No prometer en la call.** Precios y tiempos van en la propuesta, nunca en la llamada.
- **12:12.** La propuesta sale al siguiente 12:12 despues de la discovery.

## Event Log

Todas las acciones de este agente se registran en `agents/event-log.jsonl` con formato:

```json
{"agent": "discovery", "action": "[prep|analizar|oportunidades]", "project": "[id]", "timestamp": "[ISO 8601]", "details": {}}
```

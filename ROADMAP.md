# ROADMAP — MallaTierra

> **Versión:** 0.1 — planificación inicial.  
> **Documento rector:** [README.md](./README.md). Bitácora de continuidad: [AVANCE.md](./AVANCE.md).  
> **Estado global:** etapa 0 ABIERTA; etapa 1 EN ESTUDIO (documentos recibidos, lectura y comprobaciones parciales). Sin motor implementado ni validado.  
> **Orden:** las etapas se cierran con evidencia, no solo con código. **La etapa 10, optimizador del diseño físico, es la última.**

## Cómo usar este roadmap

- Marcar `[x]` únicamente cuando exista el entregable y se hayan satisfecho sus criterios de aceptación; `[ ]` significa pendiente.
- Al iniciar una sesión, revisar: **etapa activa**, **decisiones confirmadas**, **bloqueos**, **próxima tarea concreta** y **pruebas afectadas**.
- Cuando una norma, dato o hipótesis esté sin comprobar, escribir **PENDIENTE / NO CONFIRMADO**; no convertirlo en un valor predeterminado.
- Cada ecuación implementada necesitará referencia verificable a la edición normativa, explicación de variables y unidades, hipótesis, dominio de aplicación, test independiente y correspondencia con el informe.
- En módulos de seguridad eléctrica, un resultado `no evaluable` o `fuera de alcance` es preferible a una conclusión falsamente positiva.
- Los criterios de seguridad informática se revisan **en todas las etapas**, además de la revisión integral de la etapa 9.

### Registro de avance (actualización manual)

| Campo | Valor inicial |
|---|---|
| Etapa activa | 0 — Definición y preparación |
| Última revisión | 2026-11-17 |
| Entregables iniciales | `README.md`, `ROADMAP.md` y `AVANCE.md` en GitHub público (documentación de planificación) |
| Bloqueo principal | Se identificó IEEE Std 80-2013 con Cor 1-2015; pendientes estudio exhaustivo, validación independiente y delimitación de alcance |
| Otra decisión pendiente | Delimitar el primer tipo de instalación |
| Próximo paso | Completar tareas de seguridad/alcance de etapa 0 y continuar estudio crítico IEEE Std 80 (§§11, 13–17), sin motor |

## Etapa 0 — Definición, repositorio y seguridad de base

**Objetivo:** fijar qué se construirá, cómo se verificará y qué nunca se publicará.

- [x] Documentar el objetivo, la arquitectura inicial y los límites del proyecto en `README.md`.
- [x] Ordenar el desarrollo en etapas verificables en `ROADMAP.md`.
- [ ] Confirmar el primer campo de aplicación (tipo de instalación) y sus límites.
- [x] Crear el repositorio **público** con un nombre definitivo o provisional y estructura mínima ([Prowess6117/c-oSPT](https://github.com/Prowess6117/c-oSPT), rama `main`).
- [ ] Preparar `.gitignore`, licencia adecuada para código propio, política básica de contribución y revisión de secretos.
- [ ] Determinar tratamiento de datos reales: ubicación, mediciones, nombres de clientes, informes y archivos exportados.
- [ ] Documentar un procedimiento para cambios (`branch`/PR o equivalente), pruebas y revisiones de seguridad antes de publicar.
- [ ] Registrar decisiones tecnológicas solo después de compararlas con alternativas simples.

**Entregable:** repositorio limpio y documentación de alcance/seguridad.  
**Criterio de cierre:** no hay información privada ni normas protegidas en el repositorio; se conocen el público objetivo, el campo de aplicación inicial y las reglas de trabajo.

## Etapa 1 — Lectura técnica y matriz normativa IEEE Std 80

**Objetivo:** comprender la norma antes de traducir ecuaciones a software.

- [ ] Recibir el documento y verificar título, **edición**, correcciones y su procedencia.
- [ ] Identificar objetivo, alcance, exclusiones, hipótesis y terminología de la edición recibida.
- [ ] Levantar el flujo de cálculo y las dependencias entre variables (suelo, falla, geometría, conductor, resistencia, GPR, paso, contacto y demás verificaciones pertinentes).
- [ ] Registrar ecuaciones, tablas, factores, restricciones y ejemplos **mediante referencias propias, sin copiar la norma protegida al repositorio**.
- [ ] Distinguir procedimientos de aplicación general y casos que requieren condiciones especiales o métodos más avanzados.
- [ ] Revisar relación y posibles diferencias con DS N.º 8/2019, pliegos RIC, DS N.º 109/2017, pliegos RPTD y otros documentos que realmente apliquen.
- [ ] Crear una **matriz de trazabilidad normativa**: requisito/método → referencia exacta → entrada → salida → condición → futura prueba.
- [ ] Identificar ejemplos de referencia legalmente utilizables y sus resultados esperados.

**Entregable:** matriz normativa y esquema trazable del método, con vacíos y asuntos por resolver.  
**Criterio de cierre:** no quedan fórmulas propuestas sin identificación de su fuente y sus restricciones; cualquier vacío bloqueante está declarado.

### Evidencia parcial de etapa 1 — 2026-11-17

- **Documento publicado:** [Estudio IEEE 80/81 + RIC/RPTD y pruebas exploratorias](./docs/estudios/ESTUDIO_NORMATIVO_IEEE80_IEEE81_RIC06_RPTD06.md).
- **Identificado:** IEEE Std 80-2013, edición publicada en mayo de 2015 con Cor 1-2015; IEEE Std 81-2012; RIC N°06 y RPTD N°06 según copias adjuntas, sin subir los PDF.
- **Pruebas exploratorias:** diez comparaciones numéricas del anexo B.1–B.4 (R_g, E_m, E_s), consistencia Wenner IEEE 81, efecto de redondeo de C_s y una comprobación de conductor de cobre. **No validan el motor ni certifican cumplimiento**.
- **Hallazgo crítico abierto:** discrepancia aritmética de la alternativa de conductor cobre-acero del anexo B.1: valor publicado 59,81 kcmil frente a ≈65,90 kcmil al sustituir literalmente las constantes. No usarla como referencia de validación hasta resolverla.
- **Estado de cierre:** etapa 0 sigue abierta; etapa 1 iniciada pero NO cerrada. Mantener casillas pendientes hasta verificar todos sus criterios.

### Continuación de las verificaciones — 2026-11-17

Se publicó y cotejó en `main` el [conocimiento consolidado](./docs/estudios/CONOCIMIENTO_CONSOLIDADO_ETAPA1.md), la [bitácora de comprobaciones adicionales](./docs/estudios/VERIFICACIONES_ADICIONALES_ETAPA1_2026-11-17.md) y un [script autónomo de pruebas exploratorias](./docs/estudios/pruebas_exploratorias_2026_11_17.py) (no es motor del producto).

**Comprobado con evidencia aritmética parcial:** térmica cobre ec. (47); `K_f` de 30 % cobre-acero a 1084 °C; cinco valores de `D_f` frente a tabla 10; reparto `S_f` en el ejemplo simplificado de §15.9; Schwarz sintético y consistencia de su matriz de resistencias; Wenner con control de profundidad y registros seleccionados de H.1; resistencia/GPR del benchmark H.3.1.

**No resuelto / bloqueante:** resultado de cobre-acero del anexo B.1 (59,81 kcmil publicado frente a ≈65,905 de sustitución directa) y tensiones `E_m/E_s` del anexo H.3.1 (diferencia ≈4,5–4,7 % en reconstrucción). Siguen pendientes validaciones independientes, modelos de capas, factores de reparto de redes complejas, límites de dominio, casos especiales y correlato con normativa chilena. **No se marca cierre de etapa 0 ni etapa 1 y no se autorizan funciones de ingeniería.**

## Etapa 2 — Modelo de datos, flujo y prototipo mínimo

**Objetivo:** diseñar los datos sin confundir mediciones, hipótesis y resultados.

- [ ] Definir unidades y convenciones: `m`, `Ω·m`, `Ω`, `A`, `kA`, `s`, `mm²`, `V`, entre otras pertinentes.
- [ ] Catalogar entradas obligatorias, opcionales y calculadas; identificar las que deben bloquear el cálculo si faltan.
- [ ] Definir procedencia de entrada: medido / informado / interpretado / calculado / criterio explícito del proyectista.
- [ ] Modelar escenarios, geometría, restricciones de terreno, suelo, falla, materiales, electrodos y versiones normativas.
- [ ] Diseñar estados de validación: `cumple`, `no cumple`, `no evaluable`, `fuera de alcance`.
- [ ] Diseñar formato estructurado y versionado para exportar/importar proyectos, sin datos privados de muestra.
- [ ] Crear una interfaz mínima, **sin afirmar resultados todavía**, para recorrer entradas, avisos y errores.
- [ ] Elegir e instalar herramientas de pruebas, análisis estático y control de dependencias, tras revisión de seguridad.

**Entregable:** esquema de datos, validadores básicos y prototipo inicial.  
**Criterio de cierre:** datos críticos no se autocompletan; todas las entradas tienen unidad, validación y procedencia; los casos de prueba no requieren datos privados.

## Etapa 3 — Integración del estudio de resistividad

**Objetivo:** recibir, documentar y comprobar el modelo geoléctrico obtenido por medios externos.

- [ ] Definir qué resultados de IP2Win (o similar) se ingresarán y en qué formato.
- [ ] Registrar mediciones originales, configuración de electrodos, instrumento y trazabilidad **cuando se disponga de esos datos**.
- [ ] Distinguir resistividad aparente, parámetros del modelo interpretado y resistividad equivalente, cuando corresponda.
- [ ] Revisar métodos de cálculo o aproximación de resistividad equivalente **solo desde fuentes verificadas y bajo condiciones de aplicación explícitas**.
- [ ] Comparar resultados con una planilla Excel y casos independientes; registrar unidades y tolerancias justificadas.
- [ ] Detectar valores inconsistentes, configuraciones no admitidas o faltas de información.
- [ ] Separar el módulo geoléctrico del motor de cálculo de mallas para permitir mejoras posteriores.

**Entregable:** módulo de entrada y validación de resistividad/modelo de suelo, con evidencias de contraste.  
**Criterio de cierre:** es posible rastrear cada parámetro de suelo hasta su estudio o supuesto; no se acepta automáticamente una equivalencia inapropiada.

## Etapa 4 — Geometría, reticulado, conductores y condiciones de falla

**Objetivo:** representar diseños candidatos y sus entradas eléctricas sin introducir geometrías que el método no puede resolver.

- [ ] Modelar mallas rectangulares de dimensiones `m × n` en metros y su reticulado, diferenciando **dimensiones** de **cantidad de conductores o cuadrículas**.
- [ ] Definir ubicación, separación, cantidad y longitud de conductores; profundidad y electrodos, según el método aplicable.
- [ ] Definir propiedades del material y criterios térmicos respaldados documentalmente.
- [ ] Registrar magnitudes de falla, duración, reparto de corriente y demás datos del sistema que la norma exija; **sin adoptar valores típicos sin autorización**.
- [ ] Incorporar restricciones geométricas explícitas: área disponible, obstáculos, límites constructivos y otras que defina el proyecto.
- [ ] Rechazar geometrías y parámetros fuera del dominio de las fórmulas elegidas.
- [ ] Preparar un dibujo esquemático que no sustituya las dimensiones numéricas de referencia.

**Entregable:** modelo geométrico/electrotécnico verificable.  
**Criterio de cierre:** datos, distancias, longitud total, cantidades y restricciones son reproducibles; ninguna geometría no soportada se calcula como válida.

## Etapa 5 — Motor de cálculo y verificaciones IEEE Std 80

**Objetivo:** implementar de manera modular y auditable el procedimiento que resulte aplicable tras la etapa 1.

- [ ] Implementar cálculo térmico/selección de conductor cuando corresponda al caso estudiado.
- [ ] Implementar resistencia de malla y/o puesta a tierra con las ecuaciones y modelos de suelo admitidos.
- [ ] Implementar determinación de la corriente pertinente para la malla y la elevación de potencial de tierra (GPR), según datos y método confirmados.
- [ ] Implementar valores admisibles de tensiones de paso/contacto, con sus hipótesis explícitas.
- [ ] Implementar estimaciones de tensiones de paso/contacto y factores geométricos pertinentes, respetando sus restricciones.
- [ ] Comparar resultados calculados y admisibles; agregar estados de `no evaluable` y `fuera de alcance`.
- [ ] Documentar para cada función la fuente, fórmula, unidades, condiciones y errores esperables.
- [ ] Evitar dependencias de interfaz, red o almacenamiento dentro del motor numérico.

**Entregable:** biblioteca de cálculo por módulos y comprobadores de consistencia.  
**Criterio de cierre:** cada salida puede auditarse desde las entradas y cada procedimiento tiene su trazabilidad normativa; ninguna salida inválida se informa como aprobada.

## Etapa 6 — Validación matemática, ingeniería y regresión

**Objetivo:** demostrar que el software calcula correctamente **dentro de su alcance declarado**.

- [ ] Contrastar ejemplos de referencia aplicables y autorizados, incluida la edición exacta de la norma.
- [ ] Contrastar procedimientos con cálculo manual y Excel **independientes del código**.
- [ ] Establecer tolerancias numéricas justificadas por precisión, redondeos y método.
- [ ] Probar valores extremos, ceros, errores de unidades, modelos incompatibles, datos omitidos y geometrías límites.
- [ ] Registrar casos conformes, no conformes y no evaluables, evitando pruebas que solo repliquen la misma ecuación defectuosa.
- [ ] Implementar pruebas unitarias, de integración y regresión; ejecutar automáticamente antes de fusionar cambios.
- [ ] Documentar divergencias y no habilitar un módulo inseguro mientras no se resuelvan.

**Entregable:** batería de pruebas, comparativas y registro de diferencias.  
**Criterio de cierre:** resultados representativos concuerdan con referencias independientes dentro de tolerancias justificadas y se conocen las limitaciones restantes.

## Etapa 7 — Interfaz utilizable, visualización y PWA local-first

**Objetivo:** convertir el motor validado en un flujo de trabajo comprensible y manejable desde distintos PC.

- [ ] Formularios por etapas con unidades visibles, explicación de parámetros y advertencias claras.
- [ ] Visualizar terreno, geometría y reticulado con una escala coherente, sin alterar los valores del motor.
- [ ] Permitir comparar escenarios y mostrar resultados con su procedencia y estado de verificación.
- [ ] Incorporar guardado/exportación e importación local **sin sincronización remota involuntaria**.
- [ ] Habilitar características PWA cuando estén justificadas y probadas (manifest, instalación y operación offline).
- [ ] Verificar accesibilidad básica, errores de usuario y compatibilidad con navegadores objetivo.
- [ ] Evitar que el navegador cachee, divulgue en URL o transmita expedientes técnicos.

**Entregable:** aplicación local-first usable sin servicio de cálculo remoto.  
**Criterio de cierre:** los cálculos siguen funcionando sin backend y el usuario entiende qué está comprobado y qué no.

## Etapa 8 — Informe técnico de malla a tierra

**Objetivo:** producir un documento verificable y adecuado para revisión profesional.

- [ ] Establecer estructura: objetivo/alcance, antecedentes, normativa, suelo, parámetros, metodología, geometría, cálculos, verificaciones, observaciones y conclusiones.
- [ ] Incluir ecuaciones o referencias, sustitución mínima de valores, unidades y versiones de cálculo suficientes para trazabilidad.
- [ ] Identificar datos medidos, proporcionados, interpretados y supuestos del proyectista.
- [ ] Incorporar tablas, diagramas y comparación de alternativas cuando proceda.
- [ ] Mostrar advertencias, incumplimientos, limitaciones y elementos no evaluables **sin ocultarlos**.
- [ ] Generar informe local imprimible/PDF; verificar formato y metadatos para no exponer datos accidentales.
- [ ] Ensayar informes de ejemplo con datos ficticios; revisar legibilidad, cálculo y consistencia con la interfaz.

**Entregable:** generador de informes técnicos y plantilla de informe auditada.  
**Criterio de cierre:** cada conclusión se puede vincular a un cálculo y una fuente; el documento no implica certificación automática.

## Etapa 9 — Revisión integral de seguridad, publicación y operación

**Objetivo:** hacer viable el uso desde varios PC mediante un repositorio público, sin exponer datos privados ni introducir servicios innecesarios.

- [ ] Auditar repositorio e historial en busca de secretos, datos personales, ubicaciones y archivos con licencia restringida.
- [ ] Auditar dependencias y licencias; fijar versiones, revisar vulnerabilidades y configurar actualizaciones deliberadas.
- [ ] Revisar comunicaciones salientes, analítica, CDN, tipografías, mapas, errores, almacenamiento y caché offline.
- [ ] Probar importación de archivos malformados, inyección HTML, contenido excesivo, errores de exportación y nombres peligrosos.
- [ ] Aplicar las protecciones web compatibles con el alojamiento elegido (por ejemplo CSP cuando corresponda).
- [ ] Documentar que GitHub Pages puede registrar IP de visitantes y que no se promete anonimato absoluto.
- [ ] Documentar límites de seguridad en computadores compartidos, navegadores comprometidos y extensiones.
- [ ] Probar build, pruebas automáticas y despliegue desde una instalación limpia, sin tokens embebidos en cliente.
- [ ] Decidir por separado si habilitar GitHub Pages o mantener uso local, según el resultado de la auditoría.
- [ ] Etiquetar una versión estable del motor y del generador de informes como **línea base para el optimizador**.

**Entregable:** versión base publicada o lista para ejecutar localmente, con procedimiento de actualización y amenazas conocidas.  
**Criterio de cierre:** revisión técnica y de seguridad registrada; no existen envíos de datos de proyecto por defecto; datos sensibles nunca han sido publicados deliberadamente.

## Etapa 10 — OPTIMIZADOR DEL DISEÑO FÍSICO DE LA MALLA (ÚLTIMA ETAPA)

**Objetivo:** incorporar un botón **«Proponer optimización»** que, partiendo de una malla inicial `m × n`, busque diseños más convenientes de dimensiones y reticulado **sin comprometer las verificaciones** del motor validado.

### 10.1. Definición del problema

- [ ] Precisar qué se entiende por «mejor»: por ejemplo, **menor longitud de conductor**, menor cantidad de electrodos, aprovechamiento de terreno o menor costo, si se dispone de precios reales. Permitir más de un criterio sin reducir toda la seguridad a un número arbitrario.
- [ ] Definir variables que se pueden modificar y aquellas que permanecerán fijas por decisión del proyectista.
- [ ] Ingresar límites geométricos de la zona aprovechable, obstáculos, zonas excluidas y restricciones constructivas, cuando corresponda.
- [ ] Establecer restricciones eléctricas **verificadas**: paso/contacto admisibles, estado térmico, resistencia/GPR cuando el caso y la exigencia aplicable lo requieran.
- [ ] Respetar que la geometría y el modelo de suelo deben estar **dentro del dominio de las fórmulas o del método de análisis**. Para terrenos irregulares no se extrapolarán automáticamente ecuaciones para mallas rectangulares.

### 10.2. Estudio de algoritmos y aproximaciones

- [ ] Analizar si procedimientos de aproximación sucesiva, promedios, búsqueda por intervalos o interpolación pueden ofrecer candidatos útiles **sin suponer que son fórmulas de IEEE 80**.
- [ ] Estudiar inicialmente búsqueda discreta y barridos de parámetros (dimensiones, separaciones y reticulados) con restricciones explícitas.
- [ ] Considerar búsqueda progresiva de grueso a fino, optimización multiobjetivo o heurísticas adicionales solo cuando aporten resultados reproducibles y comprobables.
- [ ] Determinar si existe monotonía o continuidad suficiente antes de usar un método que dependa de ellas (por ejemplo bisección). No aplicarlo por intuición.
- [ ] Evaluar desempeño computacional y presupuestos máximos de búsqueda **sin sacrificar validación**.

### 10.3. Implementación y control técnico

- [ ] Generar candidatos a partir de la malla inicial y de los límites del terreno, sin cambiar parámetros críticos sin consentimiento.
- [ ] Calcular **cada candidato** con el mismo motor validado de la etapa 5, incluida verificación de dominio y errores.
- [ ] Descartar candidatos geométricamente imposibles, técnicamente no evaluables o que incumplan restricciones obligatorias.
- [ ] Ordenar solo soluciones admisibles según el criterio escogido; cuando ninguna sea viable, mostrar **«sin solución viable en el espacio evaluado»**.
- [ ] Comparar malla original y opciones: dimensiones, reticulado, conductores, electrodos, magnitudes calculadas, márgenes, costo si está fundamentado y restricciones activas.
- [ ] Conservar bitácora reproducible: algoritmo, variables, límites, número de candidatos, descartes, versión del motor y criterios de selección.
- [ ] Incorporar la comparación y las limitaciones de la búsqueda al informe técnico.
- [ ] Probar contra casos con solución conocida o enumeración completa posible y con casos inviables.

**Entregable final:** optimizador explicable de configuraciones físicas que propone y compara mallas **ya verificadas**.

**Criterio de cierre:** al pulsar el botón, la app propone configuraciones dentro de los límites ingresados, explica sus resultados y jamás transforma un cálculo no válido en «cumple». Si la búsqueda es parcial o heurística, informa **«mejor alternativa encontrada»**, no «óptimo global».

---

## Matriz de decisiones pendientes

| ID | Decisión | Estado | Cómo resolverla |
|---|---|---|---|
| D-01 | Edición/correcciones de IEEE Std 80 | **PENDIENTE** | Revisar PDF que aportará el usuario |
| D-02 | Primer tipo de instalación objetivo | **PENDIENTE** | Delimitar tras identificar alcance de la norma y contexto chileno |
| D-03 | Procedimiento y entradas de resistividad | **PENDIENTE** | Definir desde IP2Win/Excel y estudio técnico |
| D-04 | Lenguaje/framework/UI | **PENDIENTE** | Comparar soluciones simples, offline y seguras |
| D-05 | Persistencia de casos y cifrado | **PENDIENTE** | Evaluar modelo de amenazas y flujo de archivos |
| D-06 | Alojamiento en GitHub Pages | **CONDICIONAL** | Solo tras auditoría de etapa 9 |
| D-07 | Alcance de optimización geométrica | **PENDIENTE** | Depende del motor y dominio de fórmulas ya validados |

## Plantilla para cada sesión de avance

Copiar y actualizar esta ficha cuando se retome el proyecto:

```text
Fecha:
Etapa activa:
Objetivo de la sesión:
Evidencia consultada (archivo/edición/sección):
Cambios realizados:
Pruebas efectuadas y resultados:
Decisiones confirmadas:
Supuestos expresos / no confirmados:
Riesgos técnicos o de seguridad:
Bloqueos:
Próxima tarea concreta:
```

## Regla final

**Primero comprender → después implementar → validar → documentar → publicar con seguridad → y solo entonces optimizar el diseño físico.**
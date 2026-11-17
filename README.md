# MallaTierra — Diseño y verificación de mallas de puesta a tierra

> **Estado:** etapa 0 cerrada **documentalmente con excepciones de seguridad registradas**; etapa 1 cerrada como estudio documental acotado; motor todavía sin implementar ni validar.  
> **Uso previsto:** herramienta personal de apoyo a la ingeniería eléctrica en Chile.  
> **Documentos complementarios:** [ROADMAP.md](./ROADMAP.md) (plan), [AVANCE.md](./AVANCE.md) (continuidad) y [BACKUP_DOCUMENTAL.md](./BACKUP_DOCUMENTAL.md) (punto de recuperación de etapa 0).  
> **Nombre «MallaTierra»:** provisional; podrá cambiarse sin alterar el alcance.

## 1. Propósito

Desarrollar una aplicación **web instalable (PWA), local-first y, en lo posible, funcional sin conexión**, para ingresar antecedentes, dimensionar y verificar mallas de puesta a tierra, comparar alternativas y generar **informes técnicos trazables**.

El fundamento técnico principal será **IEEE Std 80-2013, según ejemplar recibido que incorpora Cor 1-2015**. La **etapa 1 se cerró únicamente como estudio documental acotado** de procedimientos aplicables a mallas regulares de subestaciones de CA en suelo uniforme justificado. La selección formal del ámbito de la primera versión, la revisión de exigencias de cada proyecto y la **validación del futuro motor** siguen pendientes. No se presenta el estudio documental como validación computacional ni certificación. Se revisará su campo de aplicación y su relación con la normativa chilena pertinente a cada caso. **No se asumirá que IEEE 80 es aplicable indiscriminadamente a cualquier instalación eléctrica.**

El objetivo es construir una **herramienta de cálculo auditable**, no una caja negra que entregue una respuesta sin justificarla. El desarrollo prioriza, en este orden:

1. Seguridad de las personas y corrección del método técnico.
2. Trazabilidad normativa y reproducibilidad de resultados.
3. Protección de datos y seguridad informática.
4. Facilidad de uso, generación documental y acceso desde distintos computadores.
5. Mejora progresiva del diseño mediante un optimizador, **solamente al final**.

## 2. Resultado final esperado

Para un caso dentro del campo de aplicación confirmado, la herramienta debería permitir:

1. **Definir el caso:** identificación opcional del proyecto, tipo de instalación, referencias, versiones de normas, origen de datos y condiciones especiales.
2. **Incorporar el estudio de resistividad:** registrar datos de medición e interpretación, usando inicialmente resultados producidos fuera de la aplicación (IP2Win o software similar) y su comprobación con fórmulas y Excel. No se pretende replicar IP2Win en la primera versión.
3. **Definir el terreno y el modelo de suelo:** geometría disponible, restricciones y parámetros de resistividad; declarar explícitamente si el modelo utilizado es compatible con el método de cálculo seleccionado.
4. **Definir condiciones eléctricas y criterios de diseño:** datos de falla, tiempos, reparto de corrientes y los demás parámetros que el procedimiento aplicable requiera, sin completarlos silenciosamente.
5. **Plantear una malla inicial:** dimensiones en metros (por ejemplo, `m × n`), número/disposición de conductores, reticulado, profundidad, electrodos verticales y materiales, según corresponda.
6. **Ejecutar cálculos y verificaciones:** resistencia de puesta a tierra, elevación de potencial de tierra (GPR), tensiones de paso/contacto, evaluación térmica del conductor y otras magnitudes **en la medida que sean pertinentes y estén fundamentadas en la norma aplicable**.
7. **Analizar y comparar alternativas:** distinguir resultados calculados, límites admisibles, márgenes de seguridad, hipótesis y estados `cumple / no cumple / no evaluable`.
8. **Emitir un informe técnico:** datos de entrada, procedencia, metodología, ecuaciones, sustituciones mínimas, unidades, resultados, verificaciones, advertencias, referencias y conclusiones. El informe no debe aparentar una aprobación normativa cuando la evidencia sea insuficiente.
9. **Optimizar la configuración de la malla (última etapa):** a partir de una geometría y un reticulado inicial, proponer configuraciones candidatas que aprovechen mejor el terreno y los materiales, **sin omitir ninguna verificación eléctrica o de seguridad**.

## 3. Alcance inicial y límites

### En alcance

- Estudio documental y trazable de IEEE Std 80 antes de programar ecuaciones.
- Implementación de **métodos explícitamente identificados**, con sus condiciones de aplicación.
- Flujo inicial de resistividad **externo** a la aplicación, con ingreso de resultados, procedencia y contraste independiente.
- Geometrías regulares en una primera implementación, siempre que los métodos elegidos las admitan; geometrías irregulares quedan condicionadas a la existencia de métodos verificables adecuados.
- Múltiples escenarios y comparación de diseños, cuando el motor esté validado.
- Generación local de informes y exportación/importación consciente de datos.
- Repositorio público para el **código**, pruebas con datos sintéticos o autorizados y documentación propia.

### Fuera de alcance inicial

- Ejecutar automáticamente una inversión geofísica equivalente a IP2Win.
- Simulación electromagnética avanzada, cálculo por elementos finitos o modelos arbitrarios sin validación específica.
- Certificar, aprobar o sustituir la revisión/firma del profesional competente.
- Declarar «seguro» un diseño únicamente porque su resistencia a tierra es baja.
- Publicar estudios reales, ubicaciones, archivos de clientes, credenciales, claves, tokens o datos sensibles.
- Almacenar proyectos de ingeniería en una base de datos remota o sincronizarlos automáticamente.

### Ámbito normativo por confirmar

IEEE Std 80 se orienta principalmente a la seguridad de sistemas de puesta a tierra de **subestaciones de corriente alterna**. Antes de fijar las funciones definitivas hay que precisar qué instalaciones serán cubiertas en la primera versión y cuáles requerirán otros enfoques. Se revisarán, según la instalación, el **DS N.º 8/2019 y pliegos RIC**, el **DS N.º 109/2017 y pliegos RPTD**, y las demás exigencias aplicables. **No se atribuyen por adelantado requisitos o numerales específicos a esos textos.**

## 4. Principios de ingeniería y trazabilidad

- **Evidencia antes de cálculo:** falta de un dato crítico = cálculo bloqueado o resultado `no evaluable`, nunca valor inventado.
- **Origen de cada dato:** `medido`, `informado por tercero`, `interpretado`, `calculado` o `supuesto explícito del proyectista`.
- **Unidades siempre visibles:** conversión de unidades controlada y comprobada.
- **Método identificado:** edición, sección/ecuación de referencia y restricciones; se registrarán después de estudiar el texto normativo real.
- **Modelos compatibles:** no reutilizar ecuaciones para suelos, topologías o rangos fuera de sus hipótesis sin justificación y validación.
- **Estados diferenciados:** `cumple`, `no cumple`, `no evaluable` y `fuera del campo de aplicación`.
- **Resultados reproducibles:** mismos datos, mismo método y misma versión del motor deben producir los mismos resultados dentro de tolerancias declaradas.
- **Validación independiente:** ejemplos autorizados de referencia, comprobaciones manuales/Excel y ensayos de frontera; un resultado que coincide consigo mismo no constituye validación.
- **Documentación honesta:** no usar el nombre IEEE o SEC como «sello de aprobación» de la aplicación.

## 5. Arquitectura propuesta (decisión inicial, revisable)

**Preferencia:** aplicación web estática **PWA**, con interfaz y cálculos ejecutados en el navegador, sin backend y sin cuentas de usuario. El código podrá alojarse en un repositorio público de GitHub y publicarse como sitio estático (por ejemplo, GitHub Pages) **solo después de una revisión de seguridad**.

- **Motor de cálculo separado de la interfaz:** funciones matemáticas puras, deterministas, probables mediante tests y sin dependencias de red.
- **Interfaz gradual:** formularios validados, vista geométrica, tablas y gráficos; primero una interfaz mínima para probar el flujo, después visualizaciones avanzadas.
- **Datos del caso:** por defecto mantenidos en la sesión de la aplicación; guardado local persistente solo cuando se diseñe y evalúe expresamente. Importación/exportación manual a archivos locales. Si el almacenamiento local persiste, debe indicarse que **no está cifrado automáticamente**.
- **Informes:** generados en el dispositivo del usuario. Formatos finales por decidir, con preferencia por salida imprimible/PDF y un formato estructurado para reabrir casos.
- **Offline:** objetivo progresivo. La instalación como PWA y el funcionamiento sin conexión dependen de compatibilidad del navegador, HTTPS/localhost y una estrategia de caché probada.
- **Sincronización:** GitHub sincroniza **código e historial de desarrollo**, no expedientes técnicos privados. Si se requiere mover un proyecto entre computadores, se usará una exportación controlada y un canal privado elegido por el usuario; evaluar cifrado según sensibilidad.

La tecnología concreta (lenguaje, framework, bibliotecas de gráficos/PDF y sistema de pruebas) se seleccionará por criterios documentados. No se impondrá una dependencia antes de evaluar utilidad, mantenibilidad, licencia, seguridad y comportamiento sin conexión.

## 6. Seguridad y privacidad: requisitos no negociables

**Modelo de amenaza inicial:** exposición involuntaria de identidad, dirección IP, ubicación, planos/estudios, credenciales, tokens, datos de clientes, archivos del computador o información de ingeniería; introducción de código malicioso mediante dependencias, extensiones o archivos importados.

### Repositorio público

- Incluir únicamente código, documentación propia y **datos ficticios o expresamente autorizados**.
- Mantener fuera del repositorio los informes reales, mediciones reales, coordenadas, rutas locales, logs, copias de seguridad, archivos de configuración privada, claves, tokens y credenciales.
- Definir `.gitignore`, revisión de cambios antes de `commit/push`, detección de secretos y protección de ramas. **`.gitignore` no borra secretos ya subidos al historial**: ante exposición, revocar/rotar de inmediato y sanear historial según corresponda.
- No publicar el PDF de IEEE Std 80 ni otras normas con derechos de autor. Solo incluir referencias bibliográficas y material propio, sin reproducción extensa de textos protegidos.
- No introducir secretos en JavaScript cliente, variables públicas de build ni herramientas analíticas.

### Aplicación web

- **Sin backend propio, analítica, rastreadores ni solicitudes de datos a terceros por defecto.** Revisar dependencias, tipografías, CDN, recursos de mapa y telemetría antes de usarlos.
- Validar tipo, tamaño y estructura de todo archivo importado. Evitar ejecución de contenido de entrada, inyección HTML, rutas peligrosas y exportaciones que permitan inyección de fórmulas en hojas de cálculo.
- Aplicar controles adecuados a una web estática: política de contenido (CSP) donde sea configurable, dependencias fijadas/auditadas, tratamiento seguro del DOM, revisión de permisos y pruebas de seguridad.
- Evitar almacenar datos sensibles en parámetros de URL, registros, herramientas de analítica, mensajes de error o cachés del service worker.
- **Caché offline:** limitarla a archivos de la aplicación y no conservar allí expedientes de usuarios sin una decisión explícita.
- **Computadores compartidos:** no asumir que los datos guardados en el navegador están protegidos frente a otros usuarios del equipo o extensiones instaladas.

### Direcciones IP y ubicación: límite explícito

Una web alojada en GitHub Pages **no puede ocultar la IP pública al proveedor de alojamiento**: GitHub documenta que registra la IP de visitantes para seguridad. Nuestro diseño sí puede evitar publicar esa IP en el repositorio o enviarla a servicios adicionales. No solicitar geolocalización del navegador. No prometer anonimato total ni seguridad absoluta.

## 7. Optimizador de mallas: objetivo final, no función inicial

El optimizador **no mejorará el rendimiento del software**; mejorará propuestas **físicas de diseño** de puesta a tierra.

**Flujo conceptual:** el usuario introduce el terreno utilizable, una malla inicial de dimensiones `m × n` (m), un reticulado y las restricciones; el sistema genera alternativas admisibles, calcula cada una mediante el motor validado, descarta opciones inválidas y ordena las restantes según criterios seleccionados.

Variables candidatas posibles, sujetas a validar su pertinencia: dimensiones, posición/orientación dentro del terreno, separación y cantidad de conductores, reticulado, longitud de conductor, número/posición de electrodos, profundidad y materiales cuando proceda. Restricciones: suelo y condiciones de falla, tensiones admisibles de paso/contacto, restricciones térmicas, límites geométricos, obras/obstáculos y límites constructivos expresamente ingresados.

**No se supone que IEEE 80 proporcione un algoritmo universal para hallar la malla óptima.** Se estudiará si son útiles procedimientos de aproximación sucesiva, búsqueda por intervalos, promedios o búsqueda discreta; **no se usará ninguna heurística por intuición como sustituto de la verificación normativa**. Inicialmente podrá tratarse de encontrar la *mejor alternativa dentro de un conjunto evaluado*, sin afirmar un óptimo global.

El optimizador deberá explicar qué modificó, por qué, qué restricciones comprobó, qué método utilizó, qué soluciones rechazó y cómo se comparan el diseño original y el propuesto. Las topologías fuera de la validez del motor se marcarán `no evaluables`.

## 8. Calidad, entregables y criterios de cierre

El desarrollo y las condiciones para avanzar están descritos en [ROADMAP.md](./ROADMAP.md). Se considerará utilizable para decisiones reales **solo un módulo cuyos métodos y resultados hayan sido documentados y validados**. Cada cambio a fórmulas, unidades o datos requerirá pruebas de regresión y control de versiones.

Entregables finales previstos:

- Código fuente legible, versionado y con pruebas.
- Documentación del ámbito normativo y matriz de trazabilidad ecuación → implementación → prueba → informe.
- Aplicación local-first accesible desde varios computadores, instalable cuando el navegador lo soporte.
- Casos de prueba documentados y comparaciones independientes.
- Informes técnicos generados localmente, con advertencias y límites explícitos.
- Optimizador de configuraciones, **solo al completar y validar las etapas anteriores**.

## 9. Decisiones pendientes

1. **Edición IEEE Std 80 para el estudio:** identificada como **IEEE Std 80-2013 con Cor 1-2015**. El estudio **documental acotado de etapa 1 está cerrado**; comprobar vigencia aplicable al proyecto real y validar de manera independiente los procedimientos en el motor antes de usarlos.
2. **Primer tipo de instalación objetivo**: delimitado para la primera implementación a subestaciones exteriores CA 50/60 Hz, mallas regulares y suelo uniforme justificado, solo como diseño y verificación parcial; ver [alcance inicial](./docs/ETAPA0_ALCANCE_INICIAL.md). La clasificación normativa de cada proyecto real sigue siendo indispensable.
3. **Datos técnicos mínimos, unidades y casos de prueba de referencia**: a definir durante la lectura y modelación.
4. **Repositorio público y publicación web**: GitHub será la fuente del código; habilitar un sitio público será una decisión separada, condicionada a revisión de seguridad.
5. **Persistencia/cifrado de proyectos**: se decidirá a partir de la sensibilidad real de los datos y un modelo de amenazas práctico.

### Registro de fundamentos y comprobaciones (etapa 1)

El material de investigación se conserva en `docs/estudios/`:
- [Estudio normativo inicial IEEE80/81 y RIC/RPTD](./docs/estudios/ESTUDIO_NORMATIVO_IEEE80_IEEE81_RIC06_RPTD06.md)
- [Conocimiento consolidado de la etapa 1](./docs/estudios/CONOCIMIENTO_CONSOLIDADO_ETAPA1.md)
- [Comprobaciones adicionales, discrepancias y límites](./docs/estudios/VERIFICACIONES_ADICIONALES_ETAPA1_2026-11-17.md)
- [Cierre documental de etapa 1: matriz y métodos delimitados](./docs/estudios/ETAPA1_MATRIZ_Y_CRITERIOS_DE_CIERRE.md)
- [Acta de 44 comprobaciones documentales](./docs/estudios/ACTA_PRUEBAS_ETAPA1_2026-11-17.md)
- [Script independiente de estudio de la etapa 1](./docs/estudios/verificaciones_etapa1_20261117.py)
- [Diagnóstico de inconsistencias B.1 y H.3: causas matemáticas y valores de referencia](./docs/estudios/DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md)
- [Script autocontenido para reproducir el diagnóstico B.1/H.3](./docs/estudios/diagnostico_inconsistencias_ieee80.py)
- [Script autónomo de comprobaciones exploratorias](./docs/estudios/pruebas_exploratorias_2026_11_17.py)

**Es investigación, no un motor validado.** PDFs IEEE/SEC, mediciones privadas y expedientes reales no se incorporan al repositorio. Para el estado efectivo, consultar ROADMAP y AVANCE vigentes.

## 10. Referencias para la planificación

- [IEEE Standards Association — IEEE Std 80](https://standards.ieee.org/ieee/80/4089/) — referencia institucional; se dispone de IEEE80-2013/Cor1-2015 para lectura privada. La etapa 1 solo cerró su estudio documental acotado; **el motor de cálculo aún no está implementado ni validado**.
- [GitHub Docs — What is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) — publicación estática y tratamiento de IP de visitantes.
- [MDN — Making PWAs installable](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable) — requisitos de instalación de una PWA.
- Normativa chilena: documentos RIC, RPTD y disposiciones complementarias que correspondan, **por revisar y citar con precisión** según el alcance definitivo.

## 11. Gobierno operativo y documentación de etapa 0

- [Alcance restringido de la primera implementación](./docs/ETAPA0_ALCANCE_INICIAL.md): mallas regulares para subestaciones exteriores CA y suelo uniforme respaldado; no supone conformidad integral.
- [Política de datos privados](./docs/POLITICA_DATOS.md): qué puede publicarse, tratamiento local y límites de privacidad.
- [ADR-0001 — Arquitectura y alternativas](./docs/ADR-0001_ARQUITECTURA_INICIAL.md): justificación de PWA local-first sin backend, elección detallada de stack diferida a etapa 2.
- [Seguridad](./SECURITY.md), [procedimiento de cambios](./CONTRIBUTING.md) y [auditoría inicial](./docs/ETAPA0_AUDITORIA_SEGURIDAD.md).

**Estado de etapa 0:** **cerrada para planificación/documentación con excepciones de seguridad aceptadas por el propietario**; 8/8 tareas documentales verificadas o resueltas por excepción explícita. **NO** significa seguridad informática certificada: `main` no está protegida, existen metadatos históricos con correo personal y no hay auditoría forense del historial. Véanse [BACKUP_DOCUMENTAL.md](./BACKUP_DOCUMENTAL.md) y [auditoría](./docs/ETAPA0_AUDITORIA_SEGURIDAD.md). La licencia beta restrictiva está publicada, pero no existe activación ni motor utilizable.

## 12. Licencia restrictiva beta y claves futuras

**[LICENSE.md](./LICENSE.md): todos los derechos reservados, código públicamente visible pero no abierto.** El uso personal/educativo no comercial requiere autorización del titular y, cuando se implemente, una clave propia. El **uso comercial está prohibido por defecto en beta**, salvo permiso escrito expreso y licencia/clave comercial específica. Toda salida de la aplicación requerirá verificación independiente por profesional competente, aun si el software está licenciado.

El sistema de claves está **solo planificado** en [licencias y activación](./docs/LICENCIAS_Y_ACTIVACION.md). En una PWA pública una clave de cliente no puede impedir totalmente que alguien modifique el código; no se publicarán claves privadas ni se prometerá protección absoluta. El motor científico y la validación tienen prioridad.

---

**Regla de gobierno:** si una función no puede justificar sus hipótesis, su fórmula o su prueba, no debe entregarse como cálculo normativamente validado.
# BACKUP_DOCUMENTAL — Línea base y cierre documental de etapa 0

> **Proyecto:** [c-oSPT](https://github.com/Prowess6117/c-oSPT)  
> **Fecha del respaldo:** 2026-11-17  
> **Origen examinado:** rama `main` en commit [`1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/commit/1ab884b039f1e3a858b8763fc0be31a1458ec1df)  
> **Naturaleza:** punto de restauración **documental y de decisiones**, no un respaldo físico externo, copia de todos los blobs ni garantía de seguridad.  
> **Cierre de etapa 0:** **DOCUMENTALMENTE CERRADA CON EXCEPCIONES EXPLÍCITAS** por instrucción del propietario. No es un cierre de seguridad técnica ni certificación.  
> **Etapa 1:** cerrada como estudio documental acotado; **etapas 2–10 no iniciadas** al realizar este registro.

## A. Objetivo original y decisiones que no pueden perderse

Desarrollar una herramienta **personal de ingeniería eléctrica para Chile**, inicialmente una **PWA estática, local-first, sin backend propio por defecto**, con código fuente público pero estudios reales privados. La aplicación futura debe importar antecedentes de resistividad interpretados inicialmente con **IP2Win o alternativa y contraste Excel**, verificar mallas de puesta a tierra según procedimientos **IEEE Std 80-2013 con Cor 1-2015** y reglamentación chilena aplicable, y generar **informes técnicos auditables**.

**Primera implementación limitada:** subestaciones exteriores de CA 50/60 Hz; mallas rectangulares/cuadradas y reticulado regular; suelo uniforme **solo cuando los antecedentes lo justifiquen**. No aplicar automáticamente las expresiones a suelos estratificados, geometrías irregulares, GIS, cercos, tensiones transferidas o repartos de falla insuficientemente caracterizados. Un caso que necesite verificaciones no implementadas queda **no evaluable/fuera de alcance**, sin veredicto global de conformidad.

**Última etapa 10:** botón para **optimizar dimensiones y reticulado físicos de la malla** dentro de límites del terreno, no rendimiento del software. Primero validar el motor; después estudiar algoritmos y comprobar individualmente cada candidato.

**Ningún motor está implementado ni validado.** Los cálculos exploratorios de etapa 1 no autorizan decisiones de ingeniería reales.

## B. Referencias inmutables para reconstruir la situación revisada

Los siguientes enlaces identifican versiones **fijadas a un commit** y no el contenido cambiante de `main`:

| Documento | Copia identificada al corte |
|---|---|
| Objetivo del proyecto | [README.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/README.md) |
| Etapas y criterios | [ROADMAP.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/ROADMAP.md) |
| Historial y decisiones | [AVANCE.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/AVANCE.md) |
| Licencia beta reservada | [LICENSE.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/LICENSE.md) |
| Datos y privacidad | [POLITICA_DATOS.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/docs/POLITICA_DATOS.md) |
| Alcance técnico v0.1 | [ETAPA0_ALCANCE_INICIAL.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/docs/ETAPA0_ALCANCE_INICIAL.md) |
| Arquitectura justificada | [ADR-0001 @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/docs/ADR-0001_ARQUITECTURA_INICIAL.md) |
| Activación futura | [LICENCIAS_Y_ACTIVACION.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/docs/LICENCIAS_Y_ACTIVACION.md) |
| Matriz normativa de etapa 1 | [ETAPA1_MATRIZ_Y_CRITERIOS_DE_CIERRE.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/docs/estudios/ETAPA1_MATRIZ_Y_CRITERIOS_DE_CIERRE.md) |
| Acta de comprobaciones | [ACTA_PRUEBAS_ETAPA1_2026-11-17.md @ `1ab884b039f1`](https://github.com/Prowess6117/c-oSPT/blob/1ab884b039f1e3a858b8763fc0be31a1458ec1df/docs/estudios/ACTA_PRUEBAS_ETAPA1_2026-11-17.md) |

El **estado vigente** tras este respaldo se consulta siempre en [README](./README.md), [ROADMAP](./ROADMAP.md) y [AVANCE](./AVANCE.md). En caso de desvíos, comparar sus versiones actuales con los enlaces fijados y con el historial de commits/PR. **No reescribir historia para aparentar que un control de seguridad estuvo activo.**

## C. Verificaciones realmente efectuadas antes del cierre documental

1. GitHub confirmó repositorio **público**, rama `main`, dos PR de documentación/licencia **fusionados** y commit base `1ab884b039f1e3a858b8763fc0be31a1458ec1df`.
2. Árbol de `main`: **21 archivos rastreados** antes de incorporar este backup; documentos Markdown, scripts Python exploratorios y `.gitignore`. No se encontraron PDF de normas, planillas, bases de datos ni archivos de claves por extensión en el árbol actual.
3. Se leyeron **los 21 archivos actuales** y se revisaron sus enlaces relativos; no se observaron rutas internas rotas.
4. En el **contenido actual** no aparecieron patrones evidentes de tokens habituales, bloques de clave privada ni direcciones de correo por la búsqueda aplicada; ello **no demuestra ausencia universal de secretos**.
5. Se inspeccionaron los nombres de archivos afectados por los **32 commits accesibles** de la rama `main`: no aparecieron rutas a PDF de normas, planillas, bases de datos o claves privadas como archivos versionados. **No** se analizaron de forma forense todos los contenidos de blobs históricos o forks.
6. Se detectó **un correo de autor potencialmente personal en metadatos de commits anteriores** (no reproducido aquí) y se confirmó que `main` está **sin protección** (`protected: false`).
7. No se verificó la configuración real de privacidad del correo de la cuenta ni la activación de escaneo de secretos/push protection; esas acciones administrativas **no son accesibles mediante la conexión GitHub disponible en este chat**.
8. No existe aplicación instalada, servidor, telemetría, generador de licencias, claves activas, CI de motor ni despliegue GitHub Pages probado.

**Cobertura del control:** verificación documental, de árbol y de metadatos, con búsqueda limitada de patrones. **No equivale** a un pentest ni a una auditoría de seguridad informática integral.

## D. Derechos de uso beta y claves

Se adoptó una **licencia personalizada de derechos reservados** ([LICENSE.md](./LICENSE.md)) para el código propio; no es una licencia open source. El uso personal/educativo **no comercial** requiere autorización del titular y, una vez implementado, una clave de esa modalidad. El uso comercial está **prohibido en beta salvo permiso previo expreso por escrito** más clave comercial cuando exista la activación. Las claves aún **NO EXISTEN**, y una PWA cuyo código es público no puede garantizar que el control del lado cliente sea imposible de eludir.

La licencia de uso **no equivale a aprobación técnica**. Resultados del software beta sujetos a revisión independiente por profesional competente. Antes de autorizaciones comerciales conviene evaluación jurídica de la licencia personalizada.

## E. Excepciones de seguridad asumidas al cerrar documentalmente la etapa 0

El propietario **pidió omitir por ahora la configuración administrativa** y cerrar la etapa para avanzar. El proyecto registra estas excepciones **sin afirmar que estén solucionadas**:

| ID | Excepción / riesgo residual | Estado al cierre |
|---|---|---|
| SEC-00-01 | Rama `main` sin protección ni requisito de PR impuesto por GitHub | **Abierta — aceptada provisionalmente** |
| SEC-00-02 | Correo potencialmente personal en metadatos históricos; privacidad/noreply no verificados | **Abierta — aceptada provisionalmente** |
| SEC-00-03 | Secret scanning, push protection y auditoría completa de historial no verificados | **Abierta — aceptada provisionalmente** |
| SEC-00-04 | Licencia beta personalizada sin revisión legal; activación de claves no implementada | **Abierta — implementación/revisión posteriores** |

**Consecuencia explícita:** la etapa 0 se considera **cerrada a efectos de planificación y documentación**, con **8/8 tareas documentales evaluadas**, pero **no satisface plenamente el criterio original de seguridad si este se entiende como ausencia demostrada de información personal en todo el historial**. No se debe llamar «seguridad verificada», «repositorio completamente saneado» o «protección de rama activada». No habilitar distribución de cálculos para uso real basándose en este cierre. Los riesgos quedan registrados para seguimiento, con revisiones obligatorias antes de publicación/uso profesional.

## F. Próxima sesión y reglas para recuperar el proyecto

1. Leer **README.md, ROADMAP.md y AVANCE.md de `main`** antes de responder o modificar. Contrastar este respaldo ante discrepancias.
2. **Siguiente etapa: 2**, todavía **NO INICIADA**. Primero definir entradas, unidades, contratos de datos, estados no evaluables, validaciones y pruebas. Mantener la secuencia del roadmap.
3. Respetar el **cierre documental acotado de etapa 1**; ver su matriz y acta. No presentar 44 comprobaciones exploratorias como validación del motor.
4. Mantener **IEEE Std 80-2013/Cor1-2015, IEEE Std 81-2012, RIC N°06 y RPTD N°06** solo en lectura privada, sin subir PDF normativos protegidos a GitHub.
5. Registrar nuevas decisiones e incidencias en **AVANCE.md**; en cada hito, actualizar **ROADMAP.md**. Abrir una nueva entrada de respaldo con fecha o commit si se necesita otro punto de recuperación, sin borrar este registro.
6. La **etapa 9** debe revisar seguridad de distribución y privacidad, sin olvidar las excepciones SEC-00-01/02/03/04. Podrán anticiparse controles preventivos que sean necesarios, pero nunca declararlos resueltos sin evidencia.

**Prompt corto para continuar:**

> Proyecto c-oSPT, repo https://github.com/Prowess6117/c-oSPT. Lee README.md, ROADMAP.md, AVANCE.md y BACKUP_DOCUMENTAL.md en main. Etapa 0: cierre documental con excepciones de seguridad SEC-00-01/04 explícitas; etapa 1: estudio documental acotado, sin motor validado; próxima etapa 2 sin iniciar. Privacidad local-first, derechos reservados beta con claves futuras. No subir normas ni datos reales. Optimizador físico solo en etapa 10. Comprueba el estado real antes de trabajar.

---

**Este archivo es un respaldo de continuidad, no reemplaza una copia externa del repositorio ni modifica las protecciones de GitHub.** Para una copia local independiente, cuando se decida, guardar un clon/exportación del repositorio en un medio privado y protegido; no almacenar expedientes en la copia pública.

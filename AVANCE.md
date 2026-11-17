# AVANCE — Bitácora de continuidad del proyecto

> **Proyecto / repositorio:** [c-oSPT](https://github.com/Prowess6117/c-oSPT)  
> **Nombre funcional provisional:** MallaTierra  
> **Última actualización:** 2026-11-17  
> **Etapa activa:** 0 — Definición, repositorio y seguridad de base (**EN CURSO; no cerrada**)  
> **Inicio del estudio detallado de IEEE Std 80:** INICIADO (documentación exploratoria y contrastes parciales; no cerrado)  
> **Cálculos del motor implementados y validados:** NINGUNO; únicamente pruebas matemáticas exploratorias externas al motor  
> **Naturaleza del documento:** síntesis de continuidad; no es una transcripción completa del chat.

## 1. Para qué existe este archivo

Este archivo conserva una **fotografía verificable del proyecto** para retomarlo en otro chat, en otro computador o después de una pausa sin perder el objetivo ni las decisiones ya tomadas.

La fuente de verdad está repartida de forma deliberada:

- **[README.md](./README.md):** finalidad, alcance, arquitectura propuesta y principios permanentes.
- **[ROADMAP.md](./ROADMAP.md):** etapas, tareas, criterios de cierre y pendientes.
- **AVANCE.md (este archivo):** estado actualizado, decisiones, hechos comprobados, riesgos, bloqueos y próximo paso.

**Regla:** ante una discrepancia, revisar las fuentes y la evidencia; no suponer que un resumen anterior reemplaza el contenido técnico o normativo.

## 2. Objetivo original que NO debemos perder

Construir una herramienta **personal de ingeniería eléctrica en Chile** para plantear, calcular, verificar y documentar **mallas de puesta a tierra** con base principal en **IEEE Std 80 (edición por confirmar)** y las normas chilenas que realmente correspondan al caso.

Se prevé una **aplicación web instalable (PWA), local-first, sin backend propio por defecto**, con código fuente público en GitHub y datos de proyectos tratados localmente y de manera privada. El objetivo es acceder al código y continuar el desarrollo desde diferentes computadores; **GitHub no es almacenamiento automático de los estudios eléctricos privados**.

El flujo funcional previsto es: antecedente de resistividad (inicialmente analizado externamente con IP2Win o alternativa y contrastado con fórmulas/Excel) → datos eléctricos y del suelo → malla inicial y reticulado → motor de cálculo normativamente fundamentado → verificaciones de seguridad → alternativas → **informe técnico trazable**.

**Última etapa del ROADMAP:** un **optimizador de la geometría física y del reticulado de la malla**. No es un optimizador del rendimiento de la aplicación. Partirá de la malla inicial `m × n`, los límites del terreno y restricciones explícitas; analizará aproximaciones o búsquedas justificables y verificará cada candidato con el motor ya validado. Si no se demuestra optimalidad global, informará «mejor alternativa encontrada», no «óptimo global».

## 3. Hechos confirmados (al 2026-11-17)

1. Se creó y conectó el repositorio público **[Prowess6117/c-oSPT](https://github.com/Prowess6117/c-oSPT)**, rama principal `main`.
2. `README.md` y `ROADMAP.md` se subieron correctamente y su presencia fue comprobada directamente en GitHub.
3. La **etapa 0 está parcialmente realizada**, no finalizada: se documentaron objetivos y etapas y se creó el repositorio, pero faltan medidas y definiciones indicadas en ROADMAP.
4. El usuario aportó **IEEE Std 80-2013 con Cor 1-2015** (ejemplar publicado 15-05-2015) e **IEEE Std 81-2012**, además de RIC N°06 y RPTD N°06. Ninguno de los PDF se publicó en GitHub.
5. **La etapa 1 está iniciada, NO cerrada**; hay matriz documental preliminar y pruebas exploratorias de ejemplos sintéticos, pero no se ha implementado el motor ni realizado validación técnica independiente integral.
6. No se subieron archivos de normas, mediciones reales, expedientes técnicos, credenciales ni datos privados al repositorio en esta preparación documental.

## 4. Decisiones y criterios registrados

| ID | Decisión o criterio | Estado |
|---|---|---|
| DEC-01 | Usar GitHub público para código y documentos no sensibles | **Confirmado** |
| DEC-02 | Preferir PWA web estática, local-first, sin backend propio | **Propuesta inicial aceptada; implementación no seleccionada** |
| DEC-03 | No reproducir IP2Win en la primera versión; admitir el modelo interpretado y contraste externo | **Definido para planificación** |
| DEC-04 | No programar ecuaciones de IEEE 80 antes de leer y documentar la edición efectiva | **Obligatorio** |
| DEC-05 | Priorizar exactitud, seguridad eléctrica, trazabilidad y pruebas independientes sobre comodidad visual | **Obligatorio** |
| DEC-06 | Generar informes auditables, sin atribuir certificación IEEE/SEC a la aplicación | **Definido para planificación** |
| DEC-07 | Mantener el optimizador geométrico como **etapa final 10** | **Confirmado** |
| DEC-08 | Mantener un resumen público de progreso, sin copiar conversaciones completas ni datos sensibles | **Confirmado** |

## 5. Pendientes y límites NO confirmados

- **Edición recibida:** IEEE Std 80-2013 con Cor 1-2015, confirmada en portada; quedan pendientes erratas posteriores, estudio exhaustivo de métodos/restricciones y controles normativos complementarios.
- **Primer campo de aplicación:** subestaciones, instalaciones industriales/consumo u otros casos; pendiente de delimitar para no extender IEEE 80 fuera de su campo.
- **Normativa chilena concreta, exigencias y numerales aplicables:** revisar RIC / RPTD y otros textos pertinentes sin inventar referencias.
- **Herramientas de programación y pruebas:** no elegidas todavía.
- **Mediciones, modelos geoléctricos, parámetros eléctricos, geometrías de cálculo, tolerancias y casos patrón:** aún no definidos.
- **Política de datos reales, persistencia/cifrado, `.gitignore`, licencia, protección de ramas y revisión de secretos:** faltan definiciones y configuraciones.
- **Publicación en GitHub Pages:** no aprobada; depende de futura auditoría de seguridad.
- **Algoritmo del optimizador:** pendiente de análisis de fundamentos matemáticos, restricciones y validez del motor.

## 6. Riesgos bajo vigilancia

- **Seguridad eléctrica:** aceptar un cálculo fuera del dominio de las fórmulas; usar solo resistencia de puesta a tierra como veredicto; suponer datos críticos; confundir un resultado de software con aprobación normativa.
- **Seguridad informática:** filtrar información privada a un repositorio público o a una dependencia/servicio; publicar secretos en commits; usar librerías o importaciones sin validación; almacenar proyectos locales sin advertir sus límites.
- **Privacidad:** una web alojada en terceros puede comunicar la IP de conexión al proveedor; una PWA no equivale a anonimato ni a cifrado automático del almacenamiento.
- **Continuidad:** declarar terminada una etapa solo por haber escrito documentación, sin satisfacer todos sus criterios de aceptación.
- **Derechos de autor:** no subir el PDF de IEEE Std 80 ni reproducir extensamente material protegido al repositorio.

## 7. Historial resumido de hitos

| Fecha | Hito | Evidencia |
|---|---|---|
| 2026-11-17 | Se acordó el objetivo: calculadora/verificador de mallas con informes y optimizador geométrico final | [README.md](./README.md) |
| 2026-11-17 | Se organizó la planificación en 11 etapas, numeradas 0–10 | [ROADMAP.md](./ROADMAP.md) |
| 2026-11-17 | Se subieron README y ROADMAP al repositorio público | [Repositorio](https://github.com/Prowess6117/c-oSPT) |
| 2026-11-17 | Se incorporó la bitácora pública de continuidad | Este archivo |

## 7 bis. Hito técnico — 2026-11-17 (estudio preliminar, sin cierre)

- **Fuente pública:** [Estudio normativo de IEEE 80, IEEE 81, RIC N°06 y RPTD N°06](./docs/estudios/ESTUDIO_NORMATIVO_IEEE80_IEEE81_RIC06_RPTD06.md).
- **Identificación bibliográfica:** IEEE Std 80-2013 incorporando Cor 1-2015; IEEE Std 81-2012. PDF recibidos y leídos localmente, **no subidos**.
- **Trabajo efectuado:** matriz de dependencias y referencias para procedimientos de suelo, corriente de falla/reparto, límites tolerables, resistencia, GPR, tensiones de malla/paso, ensayos y obligaciones RIC/RPTD. Comprobaciones matemáticas exploratorias: diez contrastes de valores anexo B.1–B.4, un ejemplo Wenner, efecto de redondeo de C_s y ejemplo térmico de cobre.
- **Resultado y cautela:** diez magnitudes B.1–B.4 con discrepancias de 0,038 % a 1,200 % respecto de valores editoriales; **no es prueba independiente de validación del motor**. Se identificó discrepancia aún sin explicación en otro cálculo térmico del anexo B.1 (59,81 vs ~65,90 kcmil). Debe estudiarse antes de utilizarlo como prueba.
- **Cambios GitHub:** nuevo documento Markdown propio y registro de continuidad; ningún PDF, dato privado ni código numérico publicado.
- **Pendientes:** cerrar etapa 0 (alcance/seguridad), examinar sistemáticamente correcciones y métodos, validar térmica/Schwarz/D_f/S_f/modelos estratificados/anexo H, obtener documentos chilenos complementarios y estudiar registros de mediciones; no desarrollar motor aún.
- **Estado:** etapa 0 en curso; etapa 1 iniciada, **NO cerrada**; etapa 10 optimizador continúa como última etapa.

## 8. Próximos pasos (máximo cinco)

1. Completar las tareas pendientes de **etapa 0** (alcance inicial, reglas de seguridad y repositorio), sin inventar criterios normativos.
2. Obtener el PDF de **IEEE Std 80**, identificar la edición y comenzar **etapa 1: lectura técnica y matriz normativa**.
3. Delimitar el primer tipo de instalación y las verificaciones chilenas realmente aplicables.
4. Registrar cada decisión metodológica con fuente, condiciones, estado y prueba pendiente.
5. Actualizar esta bitácora y ROADMAP al concluir la próxima sesión técnica importante.

## 9. Procedimiento de «backup» de continuidad

Actualizar **al finalizar una etapa**, **después de una decisión técnica relevante** y **antes de cambiar de chat**. Estas actualizaciones requieren revisión y una acción deliberada; **no se ejecutan automáticamente**.

En cada actualización:

1. Consultar README y ROADMAP actuales y comparar con el estado real del repositorio.
2. Añadir al historial un hito fechado y describir evidencia concreta (commits, archivos o pruebas).
3. Cambiar solo tareas verificadas a `[x]`; no confundir trabajo iniciado con trabajo terminado.
4. Mantener actualizados: etapa activa, lo confirmado, lo pendiente, problemas/riesgos y siguiente acción.
5. Revisar antes del commit que **no haya** coordenadas, direcciones, identidad privada, clientes, archivos reales, tokens, contraseñas, extractos protegidos ni información accidentalmente sensible.

### Plantilla para nuevos hitos

```text
Fecha:
Etapa y estado (sin iniciar / en curso / cerrada):
Objetivo abordado:
Cambios y referencias a commits/archivos:
Fuente normativa consultada (edición/sección; si no se verificó, indicar NO CONFIRMADO):
Resultados y pruebas:
Decisiones confirmadas y motivos:
Problemas pendientes / riesgos:
Siguiente acción concreta:
```

## 10. Ficha corta para abrir un nuevo chat

> Trabajaremos en el proyecto **c-oSPT**, repositorio público: https://github.com/Prowess6117/c-oSPT. Lee primero **README.md**, **ROADMAP.md** y **AVANCE.md** en la rama `main`. Se desarrolla una PWA personal, local-first, para calcular y verificar mallas de puesta a tierra mediante procedimientos verificables de **IEEE Std 80** y normativa chilena aplicable, con informe técnico auditable. Los datos de proyectos reales no se publican. Resistividad: inicialmente IP2Win/alternativa y contraste Excel. **Etapa 0 en curso**; **etapa 1 aún no iniciada** al 2026-11-17. IEEE 80 se compartirá en el chat de lectura; no inventar edición ni fórmulas. El **optimizador de dimensiones y reticulado** es la última etapa. No marcar tareas como concluidas sin evidencia. Registrar cambios y actualizar AVANCE/ROADMAP al cerrar cada sesión importante.

---

**Principio de continuidad:** documentar lo comprobado, distinguir lo pendiente y no convertir decisiones de planificación en validaciones técnicas.

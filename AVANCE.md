# AVANCE — Bitácora de continuidad del proyecto

> **Proyecto / repositorio:** [c-oSPT](https://github.com/Prowess6117/c-oSPT)  
> **Nombre funcional provisional:** MallaTierra  
> **Última actualización:** 2026-11-17  
> **Etapa activa:** 0 — Definición, repositorio y seguridad de base (**EN CURSO; no cerrada**)  
> **Etapa 1 — estudio normativo:** CERRADA DOCUMENTALMENTE (solo subalcance de método definido; no motor ni validación integral)  
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
- **Resultado histórico y revisión:** diez magnitudes B.1–B.4 con diferencias de 0,038 % a 1,200 %; no validan el motor. La diferencia térmica B.1 (59,81 vs 65,905 kcmil) fue posteriormente explicada por corriente implícita 6,184 vs 6,814 kA; ver nuevo diagnóstico.
- **Cambios GitHub:** nuevo documento Markdown propio y registro de continuidad; ningún PDF, dato privado ni código numérico publicado.
- **Pendientes:** cerrar etapa 0 (alcance/seguridad), examinar sistemáticamente correcciones y métodos, validar térmica/Schwarz/D_f/S_f/modelos estratificados/anexo H, obtener documentos chilenos complementarios y estudiar registros de mediciones; no desarrollar motor aún.
- **Estado:** etapa 0 en curso; etapa 1 iniciada, **NO cerrada**; etapa 10 optimizador continúa como última etapa.

## 7 ter. Comprobaciones adicionales y conocimiento conservado — 2026-11-17

**Documentos publicados y verificados en `main`:**
- [Conocimiento consolidado etapa 1](./docs/estudios/CONOCIMIENTO_CONSOLIDADO_ETAPA1.md): fuente, alcance, variables, hipótesis, restricciones, criterio de continuidad y pendientes, sin copiar los PDF.
- [Verificaciones adicionales IEEE80/81](./docs/estudios/VERIFICACIONES_ADICIONALES_ETAPA1_2026-11-17.md): descripción de entradas/unidades, referencias exactas, resultados, comparaciones y discrepancias.
- [Pruebas autónomas en Python](./docs/estudios/pruebas_exploratorias_2026_11_17.py): script documental sin dependencias ni integración en la app. No es el motor del proyecto.

**Pruebas aritméticas documentadas:** térmica de cobre y `K_f` en material compuesto; cinco valores de `D_f` y efecto de 50/60 Hz; caso simplificado `S_f` de IEEE80 §15.9; Schwarz homogéneo con verificación de matriz y proporcionalidad; Wenner de IEEE81 con control `b/a` y valores seleccionados del benchmark H.1; resistencia/GPR del benchmark H.3.1. Los resultados coherentes corresponden solo a los ejemplos y condiciones especificados, **no validan un motor**.

**Discrepancias matemáticamente explicadas en estudio posterior:** B.1 `59,81 kcmil` requiere I≈6,184 kA y no I=6,814 kA; H.5/H.6 `E_m/E_s` publicados corresponden a I≈780 A, en lugar de 744,8 A indicada en H.3. Estudiadas con inversión y doble geometría; no es fe de erratas oficial.

**Bloqueos:** seguridad y primer alcance de etapa 0; validación integral de IEEE80 §§11/13–17 y anexos H/C; interpretación estratificada y estudio geoléctrico independiente; ejemplos de redes complejas `S_f`; referencia oficial y documentos complementarios chilenos. **Etapa 0 ABIERTA, etapa 1 EN CURSO, etapa 10 última, motor NO iniciado.**

## 7 quater. Resolución matemática de inconsistencias — 2026-11-17

**Informe publicado:** [DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md](./docs/estudios/DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md). **Código de reproducción:** [diagnostico_inconsistencias_ieee80.py](./docs/estudios/diagnostico_inconsistencias_ieee80.py).

**Verificación desde páginas originales del PDF IEEE80-2013/Cor1-2015:**
- **B.1:** ecuación (46) con I=6,814 kA → 65,904981 kcmil (≈33,3945 mm²). El valor editorial 59,81 kcmil sale de introducir 6,184 kA → 59,811624 kcmil. Se demuestra sustitución/transposición numérica; causa editorial histórica no ratificada.
- **H.3:** introducción y figuras H.3/H.4 fijan I_G=744,8 A. Ecuaciones (85)–(99) en Grid 1 → E_m≈221,169 V y E_s≈91,683 V; en Grid 2 → 155,266 y 76,251 V. Usando **780 A** se obtienen 231,622/96,016 V (H.5: 232/96,0) y 162,604/79,855 V (H.6: 163/80). Los GPR H.5/H.6 sí corresponden a 744,8 A.
- **Conclusión:** B.1 y H.3 **RESUELTAS MATEMÁTICAMENTE** sin cambiar fórmulas; hallazgo de probable inconsistencia editorial en valores impresos. No hay errata oficial acreditada ni validación del futuro motor.
- **Estado global:** etapa 0 ABIERTA, etapa 1 EN CURSO por otros procedimientos y controles; sin funciones de ingeniería en producción.

## 7 quinquies. Cierre verificable del estudio documental de etapa 1 — 2026-11-17

**Dictamen:** etapa 1 **CERRADA solo como estudio/documentación del subalcance inicial** de subestaciones exteriores de CA, suelo uniforme respaldado por antecedentes y geometrías regulares con método aplicable. No autoriza el uso de resultados para ingeniería real ni acredita la precisión de un motor inexistente. **Etapa 0 sigue ABIERTA (5/8 pendientes) y no se salta.**

**Evidencia incorporada a `main` y leída de vuelta tras cada publicación:**
- [Matriz integral y condiciones de cierre](./docs/estudios/ETAPA1_MATRIZ_Y_CRITERIOS_DE_CIERRE.md), 22 familias de métodos E01–E22, referencias, variables, unidades, modelos, dominios, bloqueos y pruebas futuras.
- [Acta de 44 comprobaciones matemáticas](./docs/estudios/ACTA_PRUEBAS_ETAPA1_2026-11-17.md) con comparaciones B.1–B.4, Df, Cs, tensiones tolerables, Sf/KCL, Schwarz/KVL, Wenner/sondas, modelo teórico ideal de dos capas y H.5/H.6.
- [Script de pruebas de investigación](./docs/estudios/verificaciones_etapa1_20261117.py), ejecutado localmente: **44/44 comprobaciones**, biblioteca estándar, sin acceso a red, PDF ni datos de proyectos.
- [Diagnóstico de divergencias y Cor 1](./docs/estudios/DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md): dos inconsistencias de referencias aclaradas aritméticamente, sin ratificación de fe de erratas IEEE.
- Cuatro PDF normativos empleados **solo como fuentes privadas de lectura**; no se han subido.

**Decisiones técnicas/documentales:**
1. Solo un método de suelo **uniforme y reticulado regular**, en instalaciones de CA aplicables, será candidato inicial; **no** implementar por simple sustitución para suelos de dos/múltiples capas, geometrías irregulares o GIS.
2. Riesgos de cercos, tensiones transferidas, objetos externos y retornos complejos se señalan como **no evaluables/fuera de alcance** para el primer método; si son obligatorios en una instalación, no declarar cumplimiento global.
3. La interpretación de resistividad externa (IP2Win u otra), las pruebas de módulos, su validación independiente y las mediciones de campo pertenecen a etapas posteriores. Las comprobaciones matemáticas actuales **no** validan un motor.
4. No trasladar automáticamente requisitos de RIC a RPTD; se detectó remisión potencialmente incongruente en el literal de RPTD §8.25 hacia §8.21, sin «corregirla» por cuenta propia.
5. Se verificó en IEEE-SA el estado **Inactive-Reserved** de IEEE80-2013 desde 2024-03-21; esto no implica por sí solo derogación de la remisión chilena específica. Comprobar vigencia y requisitos del proyecto real al aplicarlos.

**Criterios del ROADMAP:** los **8 ítems de estudio** se dejaron [x], respaldados por referencias; las excepciones quedaron **declaradas y bloqueadas**. La etapa 0 conserva sus 5 casillas [ ] y requiere cierre antes de ejecutar etapa 2.

**Próxima acción única:** resolver las cinco tareas pendientes de etapa 0 (alcance productivo formal, `.gitignore`/licencia/secretos, datos reales, procedimiento de revisiones y decisiones tecnológicas), luego etapa 2. **Optimizador físico: etapa 10**.

## 8. Próximos pasos (máximo cinco)

1. Completar las tareas pendientes de **etapa 0** (alcance inicial, reglas de seguridad y repositorio), sin inventar criterios normativos.
2. Respetar el **cierre documental acotado de etapa 1** y sus bloqueos; no ampliar métodos antes de fundamentarlos y validarlos.
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

> Trabajaremos en el proyecto **c-oSPT**, repositorio público: https://github.com/Prowess6117/c-oSPT. Lee primero **README.md**, **ROADMAP.md** y **AVANCE.md** en la rama `main`. Se desarrolla una PWA personal, local-first, para calcular y verificar mallas de puesta a tierra mediante procedimientos verificables de **IEEE Std 80** y normativa chilena aplicable, con informe técnico auditable. Los datos de proyectos reales no se publican. Resistividad: inicialmente IP2Win/alternativa y contraste Excel. **Etapa 0 en curso**; **etapa 1 cerrada documentalmente solo para el subalcance de suelo uniforme y mallas regulares** al 2026-11-17. PDFs de IEEE80-2013/Cor1-2015, IEEE81-2012, RIC06 y RPTD06 recibidos sin publicar; usar matriz/acta en `docs/estudios/`, mantener etapa 0 abierta y no declarar validación del motor. El **optimizador de dimensiones y reticulado** es la última etapa. No marcar tareas como concluidas sin evidencia. Registrar cambios y actualizar AVANCE/ROADMAP al cerrar cada sesión importante.

---

**Principio de continuidad:** documentar lo comprobado, distinguir lo pendiente y no convertir decisiones de planificación en validaciones técnicas.

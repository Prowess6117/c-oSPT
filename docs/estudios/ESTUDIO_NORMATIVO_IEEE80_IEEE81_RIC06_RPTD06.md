# c-oSPT — Estudio técnico documentado de puesta a tierra

**Fecha de elaboración:** 2026-11-17  
**Estado:** estudio técnico inicial avanzado; **NO constituye validación de un motor de cálculo, aprobación de ingeniería ni cierre de la etapa 1**.  
**Etapa:** 1 (en estudio), con etapa 0 aún abierta.  
**Responsabilidad:** resumen analítico y comprobaciones exploratorias; las decisiones de diseño requieren un proyectista competente y los antecedentes reales.

> **Protección de fuentes:** este documento contiene análisis original, referencias puntuales y resultados propios de recomputación. No incluye los PDF normativos, reproducción de tablas completas ni transcripciones extensas. La publicación es deliberadamente apta para un repositorio público de código; los archivos normativos deben permanecer fuera de GitHub.

## 1. Fuentes, versiones e identificación

| Código | Documento efectivamente revisado | Identificación y alcance de esta revisión |
|---|---|---|
| N-80 | *IEEE Guide for Safety in AC Substation Grounding*, **IEEE Std 80-2013** | Ejemplar publicado el **15-05-2015** que declara incorporar **IEEE Std 80-2013/Cor 1-2015**; 226 páginas de PDF. Esta edición revisa IEEE Std 80-2000. Se leyeron la introducción, el índice y las secciones clave 1, 3–9, 11–17, 19 y anexos B/H; análisis especialmente detallado de 7.4, 8.4, 13.4, 14.2, 15, 16.4–16.8 y B.1–B.4. El corrigendum indica modificaciones en cláusulas 11 y 17, anexos C y H, tablas 1 y 2 y otros elementos: **para cualquier transcripción ulterior, usar este ejemplar corregido**. |
| N-81 | *IEEE Guide for Measuring Earth Resistivity, Ground Impedance, and Earth Surface Potentials of a Grounding System*, **IEEE Std 81-2012** | 86 páginas de PDF; se revisaron alcance, seguridad, factores de error, métodos de medición e interpretación (cláusulas 1, 4–12) y anexos de modelo de suelo e instrumentación; énfasis en 5, 6, 7.2–7.4, 8 y 9. |
| C-RIC | SEC, **Pliego Técnico Normativo RIC N°06**, *Puesta a tierra y enlace equipotencial* | Documento adjunto de 27 páginas. Resolución exenta SEC N°33.877, 30-12-2020; relacionado con DS N°8/2019. Se revisaron secciones 1–12 y el alcance de la sección 13. |
| C-RPTD | SEC, **Pliego Técnico Normativo RPTD N°06**, *Puesta a tierra* | Documento adjunto de 9 páginas; Resolución exenta SEC N°33.277, 10-09-2020, **modificada por N°34.770, 22-07-2021**; relacionado con DS N°109/2017. Se revisaron cláusulas 1–9. |

**Nota de identificación:** las páginas indicadas como “página” en referencias IEEE 80 y 81 son las **páginas impresas** del cuerpo normativo, no necesariamente el número de página que muestra el visor del PDF. En RIC/RPTD se usa el número impreso del pliego. La procedencia visible de las copias recibidas no acredita por sí sola derechos de redistribución: **no redistribuir**.

**Control externo de vigencia (consulta de orientación, no dictamen jurídico):** la SEC enlaza RIC N°06 y el RPTD N°06 modificado en sus portales. Confirmar la versión vigente y resoluciones adicionales aplicables **antes de usar la herramienta en un proyecto real**:
- [SEC — pliegos RIC / DS 8](https://www.sec.cl/reglamento-de-seguridad-de-las-instalaciones-de-consumo-de-energia-electrica-decreto-08/)
- [SEC — pliegos RPTD / DS 109](https://www.sec.cl/decreto-n109-aprueba-reglamento-de-seguridad-de-las-instalaciones-electricas/)

## 2. Alcance, exclusiones y prioridades

**IEEE 80:** orientada a puesta a tierra segura de **subestaciones de corriente alterna**, especialmente exteriores (convencionales y GIS), extensible con cautela a interiores; aplicación típica a **50/60 Hz**. No cubre específicamente el diseño de subestaciones de corriente continua ni el cálculo cuantitativo de efectos de rayos (**N-80 §1.1–1.2**, p. 1–2). No debe presentarse como metodología universal para cualquier instalación de consumo.

**IEEE 81:** guía de **mediciones e interpretación**, no alternativa a resolver el diseño: resistividad, resistencia/impedancia a tierra remota, tensiones de paso/contacto, reparto de corrientes, integridad y limitaciones instrumentales (**N-81 §1.1–1.2**, p. 1–2). Las mediciones de terreno y las pruebas de inyección pueden ser peligrosas (**§5**): su ejecución corresponde a personal habilitado, con plan de seguridad y medios adecuados; c-oSPT no debe dar instrucciones de campo descontextualizadas.

**RIC N°06:** instalaciones **de consumo** de BT y MT (**C-RIC §2**, p. 1); incorpora protección de personas, equipotencialidad, dimensionamiento, inspección y condiciones de servicio. **C-RIC §5.7** remite a RPTD N°06 para sistemas de tierra cuando el suministro de una instalación es en AT o MT. No se deben trasladar sin análisis las exigencias de tierras de servicio de consumo a una malla de subestación de transporte.

**RPTD N°06:** instalaciones de producción, transporte, servicios complementarios, almacenamiento y distribución (**C-RPTD §2**, p. 1). **§8.25** remite a cálculos basados en IEEE Std 80-2013, y **§§5.1–5.3, 8.24** exigen evaluar tensiones de paso y contacto tolerables. **§8.27** incorpora una exigencia sobre valor de puesta a tierra; **no** sustituye la evaluación de gradientes.

**Hipótesis inicial de alcance para v1 (NO aprobada aún):** subestaciones de CA con geometría y modelo de suelo admitidos por el método concreto, en instalaciones regidas por RPTD N°06. Los casos RIC, MT/BT mixta, transferencias o GIS requieren clasificación normativa explícita. **D-02/etapa 0 siguen pendientes**.

## 3. Mapa de dependencias técnicas (no es código)

1. **Identificar instalación y régimen normativo**: consumo RIC, sector eléctrico RPTD, situaciones mixtas y requisitos complementarios (C-RIC §§2, 5.7, 9–10; C-RPTD §§2, 5, 8).
2. **Sondeo y modelo geoléctrico**: antecedentes de terreno y resistividad aparente → interpretación de suelo uniforme/dos capas/multicapa → decisión explícita sobre compatibilidad con el método. IEEE 81 §§6–7; IEEE 80 §§12–13. No equiparar automáticamente “resistividad aparente”, “resistividad de capa” y “resistividad equivalente”.
3. **Escenarios eléctricos y conductor**: corriente de cortocircuito relevante, camino de corriente, tiempo para solicitación térmica y material/temperatura admisible (N-80 §11.3 y §15). **La corriente máxima de un conductor no es necesariamente la corriente que se disipa desde la malla a tierra remota** (N-80 §15 y anexo B.1).
4. **Criterios fisiológicos**: tiempo de exposición al choque (`t_s`), condición de capa superficial, resistividad y criterio de masa corporal 50/70 kg, con justificación; N-80 §§5–8, especialmente §8.4. **No fijar 70 kg por defecto**: el ejemplo B.1 declara un recinto no accesible al público y explica su elección.
5. **Malla candidata**: área, dimensiones, disposición de conductores, separación, enterramiento, jabalinas/varillas y material. N-80 §9 y §16.4; RPTD §6.
6. **Resistencia y corriente de malla**: `R_g` (Ω) según modelo admitido, `I_g` (A) corriente simétrica disipable, `D_f` (adimensional), `I_G` (A) máxima corriente de malla y `GPR` (V). N-80 §§14–15 y §16.4. La división de corriente debe fundamentarse, no suponerse igual a 1 ni fijarse en 0,6 sin fuente de proyecto.
7. **Evaluación de seguridad**: estimación de `E_m` (V) y `E_s` (V) según método aplicable → comparación separada con `E_touch` y `E_step` (V). N-80 §§8.4 y 16.4–16.7. Diferenciar “verificación por cálculo” de la medición real.
8. **Condiciones especiales y trazabilidad**: cercos, portones, mandos, uniones, contactos metal-metal, tensiones transferidas, GIS y periferias; N-80 §§10, 17 y 19; N-81 §§9–10; C-RPTD §8. En ausencia de método admitido, **no evaluable/fuera de alcance**.
9. **Informe y validación de campo**: origen de datos, versión y método, cálculos reproducibles, comparación independiente, observaciones y futuras mediciones; N-80 §19 y N-81 §§8–10; C-RIC §§11–12 y C-RPTD §§8.21–8.23.

**Relaciones que no se deben confundir:** `t_c` (criterio térmico) frente a `t_s` (choque) frente a `t_f` (falla y factor decremental); `I_f` frente a `I_g`/`I_G`; `R_g` frente a `GPR`; `ρ` de suelo natural frente a `ρ_s` de recubrimiento, y frente a `ρ_a` aparente. Todos deben identificarse y justificarse caso a caso. Los símbolos se usan aquí solo como índice de variables de los documentos citados.

## 4. Matriz de procedimientos, fuentes, entradas, salidas y límites

| ID | Procedimiento / salida | Fuente exacta | Entradas mínimas a documentar | Hipótesis/advertencia y prueba futura |
|---|---|---|---|---|
| M-01 | Selección de modelo de suelo / resistividad aparente `ρ_a` | N-81 §§7.2–7.4, ecuaciones (2)–(3) para Wenner; N-80 §13 | Separación y profundidad de sondas, V/I, instrumento, fechas, orientación, interferencias | La reducción de Wenner a `2πaR` requiere sondas poco profundas con respecto al espaciamiento; **no** infiere por sí sola una estratigrafía. Prueba de límite y unidades incluida abajo. |
| M-02 | Modelo uniforme frente a dos/múltiples capas | N-80 §13.4.1–13.4.2, ecuaciones (52)–(54); N-81 §§7.3, anexos A/B | Series `ρ_a(a)`, geometría, modelo interpretado, capas y espesores | Promediar puede introducir errores no acotados; N-80 advierte específicamente contra generalizar la ecuación (53) a mallas sin varillas. **Pendiente:** caso medido y comparación independiente con modelo estratificado. |
| M-03 | Capa superficial y factor `C_s` | N-80 §7.4, ecuación (27), figura 11; C-RPTD §5.2 | `ρ` (Ω·m), `ρ_s` (Ω·m), espesor `h_s` (m) | (27) es aproximación empírica; N-80 indica proximidad dentro de un 5 % frente a método analítico en el estudio citado. Si no existe capa, norma define `C_s=1` y `ρ_s=ρ`. **Prueba numérica incluida.** |
| M-04 | Límite de tensión de paso | N-80 §8.4, ecs. (28)–(30); C-RPTD §5.1 | Masa 50/70 kg fundamentada, `t_s` (s), `C_s`, `ρ_s` | No confundir límite tolerable con tensión realmente calculada. **Prueba 70 kg con ejemplo B.1.** |
| M-05 | Límite de tensión de contacto | N-80 §8.4, ecs. (31)–(33); C-RPTD §5.2 | Ídem | Existen también criterios metal-metal (N-80 §8.4, ecs. (34)–(35)) y transferencias (§17): no quedan cubiertos por una comparación de `E_m` solamente. |
| M-06 | Conductor térmico y uniones | N-80 §11.3, ecs. (46)–(47), tablas 1/2 (corregidas); C-RPTD §§8.12–8.18; C-RIC §§7, 8 | Corriente por conductor, tiempo térmico, material, sección, temperatura inicial/final, conexiones | No usar `I_G` como sustituto automático de la máxima corriente por conductor. Depende de trayectoria, escenario y respaldo de protecciones. **Prueba puntual de cobre completada; discrepancia del ejemplo de cobre-acero señalada en §6.7. Pendiente validación térmica integral.** |
| M-07 | Resistencia inicial `R_g` suelo uniforme | N-80 §14.2, ecs. (55)–(57) | `ρ`, área `A` (m²), longitud `L_T` (m), profundidad `h` (m) | Aproximación, **no** resultado garantizado para suelo de dos capas, disposición irregular o instalaciones complejas. **Pruebas B.1–B.4 incluidas.** |
| M-08 | Resistencia de red+jabalinas (Schwarz) | N-80 §14.3 | Geometría, propiedades y configuraciones del electrodo | Pendiente estudio formal de ecuaciones (61) y relacionadas, coeficientes geométricos y comparación independiente. No sustituir por R_g simplificada universal. |
| M-09 | Corriente de malla `I_g`, factor de división `S_f` | N-80 §§15.1–15.9, ecs. (68), (70), anexo C | Falla(s), ubicación, impedancias, líneas de guardia, neutros, retornos metálicos | La corriente local del transformador puede determinar conductor, **pero no necesariamente GPR**: caso B.1. Pendiente análisis completo de reparto con fuentes de red reales/sintéticas. |
| M-10 | Corriente máxima `I_G`, factor `D_f` y `GPR` | N-80 §§15.10 y 16.4, ecs. (69), (83)–(84), y definición GPR | `I_g`, X/R, frecuencia, `t_f`, `R_g` | `D_f` no es universalmente 1; los ejemplos B usan aprox. 1 en una condición dada. **Prueba numérica GPR incluida.** |
| M-11 | Tensión máxima de malla `E_m` | N-80 §16.5.1, ecs. (85)–(96) | `ρ`, `I_G`, `K_m`, `K_i`, `L_M`, `h`, `d`, `D`, `n`, varillas | Métodos aproximados para **suelo uniforme y separación regular**; comprobar las condiciones de la configuración y de las varillas. **Pruebas B.1–B.4 incluidas.** |
| M-12 | Tensión de paso `E_s` | N-80 §16.5.2, ecs. (97)–(99) | `ρ`, `I_G`, `K_s`, `K_i`, `L_S` | Misma restricción; tensión calculada puede diferir del cálculo detallado. **Pruebas B.2 y B.4 incluidas.** |
| M-13 | Dominio del método / cómputo avanzado | N-80 §§16.7–16.8, anexo H | Modelo de suelo, malla, variación de espaciamientos, objetos conductores | §16.7 documenta contrastes en una familia de casos (áreas, geometrías, tamaños); **no constituye garantía para todo caso geométrico**. §16.8 indica simulación más detallada cuando hay dos/múltiples capas, separaciones no uniformes, objetos metálicos y geometrías fuera de límites. |
| M-14 | Casos especiales | N-80 §§10 y 17; N-81 §9.2 | Tipo de subestación, cercos, portones, tuberías, elementos metálicos externos | No presentar cálculos base como verificación de transferencia o contacto metal-metal; puede exigir tratamiento específico y medición. |
| M-15 | Verificación en terreno | N-80 §19; N-81 §§5, 8–10; C-RIC §§11–12; C-RPTD §§8.21–8.23 | Plan seguro, equipo calibrado, configuraciones de ensayo, valores brutos, incertidumbre | Solo se puede completar con mediciones documentadas efectuadas por personal competente. **No aplicable a los ejemplos sintéticos de este estudio.** |

### 4.1. Restricción cuantitativa especial del método simplificado

N-80 §16.7 explica que el contraste de sus ecuaciones de `E_m` y `E_s` se realizó en casos que **asumen suelo uniforme y espaciamiento uniforme** (incluye geometrías cuadradas, rectangulares, triangulares, T y L). Señala áreas de 6,25 a 10.000 m², entre 1 y 40 cuadrículas en un lado y separaciones de 2,5 a 22,5 m en los estudios citados. **Estos valores describen la muestra de comparación que utilizó el documento; no se reinterpretan aquí como todos los límites normativos universales**. El método exige verificar además condiciones particulares de varillas, diámetros, profundidad y ecuación usada. La extrapolación a otro dominio se marca **NO EVALUABLE** hasta disponer de método justificado.

### 4.2. Precaución con criterios de aceptación

El procedimiento N-80 §16.4 contiene **12 pasos**: preparación geoléctrica; conductor; límites tolerables; diseño inicial; resistencia; corriente de malla; evaluación de GPR; tensiones de paso/malla; comparación de límites; revisión; refinamiento; y evaluación de problemas especiales. La prueba simplificada de `GPR` frente a límite de contacto funciona como **criba temprana conservadora del procedimiento**, no como autorización para ignorar requisitos constructivos chilenos, verificación de contactos particulares o tensiones transferidas.

## 5. Matriz chilena RIC/RPTD: obligaciones distintas de las aproximaciones IEEE

| Caso / requisito | Referencia de la copia recibida | Implicación para c-oSPT |
|---|---|---|
| Seguridad más allá de una resistencia baja | C-RIC §§5.1–5.3 (p. 3) | Una resistencia reducida **no acredita por sí sola seguridad**: evaluar tensiones de paso/contacto/transferidas cuando correspondan. |
| Derivación MT/AT a pliego sectorial | C-RIC §5.7 (p. 4) | Clasificar suministro e instalación antes de seleccionar reglas y límites. |
| Tierra de servicio de consumo | C-RIC §§6.1–6.2 (p. 5) | Exigencias propias (incluida resistencia y excepciones condicionadas) **no transferibles automáticamente a RPTD**. |
| Tierra de protección en consumo | C-RIC §§7.3–7.11 (p. 6–7) | Verificar criterio de protección, conductor, continuidad y conexiones. Depende además de RIC N°05, documento **no recibido**. |
| Electrodos, conductor, tiempo y enterramiento | C-RIC §§8.7–8.12 (p. 9–10) | Considerar sección mínima y material conforme al caso; §8.8 prescribe condición de exposición **máxima de 0,5 s** en su ámbito; §8.11 profundidad mínima **0,5 m** para mallas. No universalizar en RPTD. |
| Separación e interconexión MT/BT | C-RIC §§9–10 (p. 11–12) | Requiere análisis específico de independencia/tensiones de defecto y eventual tierra común. **No resolver con un único número R_g**. |
| Medición / mantenimiento en consumo | C-RIC §§11–12 (p. 12–13) | La verificación depende de instrumentos, procedimiento, registros e inspecciones; no se completa con la aplicación. |
| Criterios paso/contacto sector eléctrico | C-RPTD §§5.1–5.3 (p. 4–5) | Evaluar 50/70 kg conforme a condiciones de proyecto; **§5.2** contiene reglas expresas para `t_s` relativas a despeje/protección de respaldo y NTSyCS: no adoptar `t_s` arbitrariamente. |
| Disposición y áreas | C-RPTD §§6–7 (p. 5–6) | Incorporar periferias, zonas críticas, tratamientos/medidas adicionales cuando corresponda. |
| Conductor, enlaces, varillas, protección y accesibilidad | C-RPTD §§8.1–8.20 (p. 6–8) | Verificar secciones, conexiones, corrosión, cercos y puntos de medición de modo independiente del cálculo de `E_m`. |
| Verificación de servicio y documentación | C-RPTD §§8.21–8.23 (p. 8) | Inspección visual, medidas de resistencia y tensiones, registros y cambios; referencia a N-81 y/o IEC 61936-1. |
| Criterio IEEE y valor de puesta a tierra | C-RPTD §§8.24–8.27 (p. 8–9) | §8.25 remite a IEEE 80-2013; §8.27 exige que el valor de puesta a tierra **no sea mayor que 20 Ω**. Este límite **no reemplaza** límites de paso y contacto de §§5 y 8.24. |

**Advertencias de interpretación:** (1) No mezclar el tiempo de exposición de **C-RIC §8.8** con el criterio de `t_s` de **C-RPTD §5.2** sin establecer cuál reglamento es aplicable. (2) La condición general de RPTD §8.27 y los límites RIC para tierra de servicio corresponden a **ámbitos diferentes**. (3) RIC remite a RIC N°05 y N°03; RPTD menciona NTSyCS y RPTD N°15; esos documentos complementarios **no se estudiaron aún y son pendientes**.

## 6. Pruebas reproducidas en entorno aislado (NO motor de c-oSPT)

**Objetivo limitado:** comprobar lectura de variables, unidades y expresión algebraica mediante cálculos transitorios ejecutados localmente, usando condiciones **sintéticas/ejemplos publicados** y comparando contra valores de referencia de la propia guía. Las implementaciones de prueba **no están integradas en el proyecto** y **no constituyen validación independiente** del método IEEE ni del software futuro.

### 6.1. Datos comunes N-80 anexo B, ejemplos B.1–B.4

`ρ = 400 Ω·m`; `ρ_s = 2500 Ω·m`; `h_s = 0,102 m`; `h = 0,5 m`; `t_f = 0,5 s`; `S_f = 0,6` **solo para los ejemplos**. El ejemplo distingue la corriente de cortocircuito de 13 kV para **dimensionar conductor** (aprox. 6814 A) de la de 115 kV usada para **corriente que produce GPR** (aprox. 3180 A). Con el supuesto ejemplar `D_f≈1`, el caso usa `I_G=1908 A`. El factor `S_f=0,6` **no es valor predeterminado de diseño**. Referencias N-80 anexo B, p. 129–134; §11.3 y §15.

### 6.2. Resistencia y tensión de malla/paso

Se recomputaron las expresiones identificadas en **N-80** §14.2 ec. (57), §16.5 ecs. (85)–(99), con los factores geométricos que corresponden a cada ejemplo. La columna de referencia procede de **N-80 anexo B** (no de la simulación EPRI adicional mencionada allí). Error absoluto porcentual referido a la magnitud publicada; el criterio de **2 % es una tolerancia de esta exploración**, NO un límite IEEE ni un criterio de aceptación de un motor.

| Ejemplo | Magnitud | Publicado en anexo B | Recomputación propia | Diferencia relativa |
|---|---|---:|---:|---:|
| B.1 — 70×70 m, sin varillas | `R_g` (Ω) | 2,78 | 2,77569 | 0,155 % |
| B.1 | `E_m` (V) | 1002,1 | 1001,61432 | 0,048 % |
| B.2 — 70×70 m; 20 varillas × 7,5 m | `R_g` (Ω) | 2,75 | 2,75264 | 0,096 % |
| B.2 | `E_m` (V) | 747,4 | 749,05861 | 0,222 % |
| B.2 | `E_s` (V) | 548,9 | 549,11079 | 0,038 % |
| B.3 — 63×84 m; 38 varillas × 10 m | `R_g` (Ω) | 2,62 | 2,61855 | 0,056 % |
| B.3 | `E_m` (V) | 595,8 | 593,61328 | 0,367 % |
| B.4 — malla L, 4.900 m²; 24 varillas × 7,5 m | `R_g` (Ω) | 2,74 | 2,74387 | 0,141 % |
| B.4 | `E_m` (V) | 761,1 | 757,18151 | 0,515 % |
| B.4 | `E_s` (V) | 574,6 | 567,70704 | 1,200 % |

**Lectura de las diferencias:** los ejemplos sustituyen factores geométricos redondeados en etapas intermedias, mientras que la recomputación mantiene decimales. Especial atención a **B.3**: el factor `n_b` de N-80 ec. (91) contiene **raíces anidadas**; las marcas de radical se pierden en cierta extracción automática del PDF. Se verificó visualmente la ecuación en p. 95 impresa (PDF p. 111). En B.4 el área real de la L (4900 m²) no coincide con el rectángulo envolvente `70×105 m`; confundirlos alteraría `n`, `K_i` y las tensiones. Estos dos puntos requieren casos de regresión futuros.

**No confundir estas coincidencias con la simulación detallada:** el anexo B muestra valores distintos obtenidos con un programa EPRI. Por ejemplo, B.2 publica `E_s=548,9 V` con su método simplificado, mientras que el programa EPRI informa `459,1 V` (diferencia aproximada de **19,6 %** respecto a la simulación). El error del método aproximado **no se estima mediante la coincidencia consigo mismo**. N-80 §16.8 y anexo H siguen siendo fuentes a estudiar para contrastes más rigurosos.

### 6.3. Factor superficial y tolerancias: efecto del redondeo

Aplicando N-80 §7.4 ec. (27) a los datos del anexo B se obtiene **`C_s = 0,74285714`** sin redondear. Si se conserva toda su precisión: `E_touch70 = 840,5479 V` y `E_step70 = 2696,0971 V` para `t_s = 0,5 s` según N-80 §8.4 ecs. (30)/(33). En **B.1** se presenta `C_s≈0,74` y con ese factor **redondeado** se recomputan `E_touch70 = 838,1690 V` y `E_step70 = 2686,5815 V`, coherentes con los valores publicados `838,2 V` y `2686,6 V`.

**Decisión recomendada para motor futuro:** conservar precisión interna completa, mostrar decimales apropiados y documentar cuándo una comparación con ejemplo publicado requiere reproducir **redondeos editoriales**, sin convertir esa coincidencia en criterio técnico general.

### 6.4. Prueba IEEE 81 Wenner (sintética, sin datos de campo)

Bajo **N-81 §7.2.3**, ecuaciones (2) y (3), se ensayó el límite de profundidad de sonda `b→0` con datos ficticios `a=2 m` y resistencia medida `R=10 Ω`. La expresión completa para `b=0` y la aproximación de sonda superficial entregan el mismo valor **`ρ_a=125,663706 Ω·m`** (diferencia numérica despreciable). La prueba verifica solamente una identidad algebraica y unidades; **no** valida un estudio de resistividad ni un modelo de dos capas.

### 6.5. Reproducción cruzada de RPTD §5.1–5.2

La presentación matemática observada visualmente en **C-RPTD p. 4, §§5.1–5.2** usa los mismos coeficientes de masa 50/70 kg, `C_s` y tiempo que las expresiones de N-80 §8.4 para límite de paso/contacto. Se confirmó la correspondencia numérica del ejemplo de 70 kg **solo con los parámetros declarados arriba**. No se derivó ninguna conformidad RPTD: falta comprobar el régimen real de tiempos, protección de respaldo, otros requisitos y vigencia exacta del proyecto.

### 6.6. Veredicto técnico de este conjunto de pruebas

- **Reproducción algebraica exploratoria:** 10 comparaciones numéricas N-80 B.1–B.4 dentro de **2 % definido para este ensayo**; identidad Wenner e identificación explícita del redondeo de `C_s` completadas; un cálculo térmico de cobre coincide, mientras que el de cobre-acero presenta discrepancia **no resuelta** (§6.7).
- **Aún NO demostrado:** validez de Schwarz, dimensionamiento térmico integral por distintos materiales, `D_f` por X/R, reparto complejo `S_f`, problemas de dos/múltiples capas, mallas no regulares, tensión transferida, GIS, cercos, ensayos de campo o conformidad integral con SEC.
- **Interpretación de seguridad:** el ejemplo B.1 **no** satisface su criterio de tensión de malla; los refinamientos posteriores ilustran el procedimiento didáctico, pero no aprueban ningún diseño real de c-oSPT. Una medición de resistencia y las verificaciones de transferencia/zonas críticas se requieren según caso.

### 6.7. Prueba adicional de dimensionamiento térmico y discrepancia detectada

Se hizo una **segunda comprobación aritmética**, independiente de las diez comparaciones de `R_g`, `E_m` y `E_s`, sobre la **N-80 §11.3.1.3, ecuación (47), y anexo B.1, p. 131**. Con los datos expresos del ejemplo (`I=6,814 kA`, `K_f=7,06`, `t_c=0,5 s`, cobre comercial), se obtiene **34,01667 kcmil** o **17,2365 mm²**, coherente con el valor editorial **34,02 kcmil / 17,2 mm²**. Esa comprobación **no** cubre dimensionamiento mecánico, corrosión ni condiciones normativas chilenas.

**Hallazgo pendiente — no corregir silenciosamente:** al sustituir literalmente los parámetros que aparecen impresos en la alternativa de **acero recubierto de cobre de conductividad 30 %** (N-80 §11.3.1.2, ec. (46), y anexo B.1 ec. (B.3), p. 131): `I=6,814 kA`, `t_c=0,5 s`, `TCAP=3,85 J/(cm³·°C)`, `α_r=0,00378 1/°C`, `ρ_r=5,862 µΩ·cm`, `K_o=245 °C`, `T_m=700 °C`, `T_a=40 °C`, la aplicación directa de la ecuación (46) con radical cubriendo el producto térmico y logarítmico entrega **≈65,90 kcmil (≈33,39 mm²)**, mientras que el anexo B.1 imprime **59,81 kcmil (30,24 mm²)**. Se inspeccionó visualmente la fórmula en la página, no solamente la extracción de texto. **No se determinó el origen de la discrepancia** (posible errata, dato redondeado, transcripción editorial u otra condición) y **no se incorporará ninguna de ambas cifras como prueba de aceptación** hasta una verificación adicional contra tablas/materiales y/o fuente independiente. No suponer que la discrepancia queda resuelta por parecer pequeña.

Este hallazgo demuestra por qué los resultados publicados deben someterse a comprobación aritmética y por qué **coincidir con un ejemplo no equivale automáticamente a validar todos los métodos**.

## 7. Registro de riesgos técnicos, normativos y de seguridad

| ID | Riesgo | Tratamiento obligatorio |
|---|---|---|
| R-01 | Elegir 70 kg y un tiempo pequeño como valores silenciosos | Entradas justificadas; distinguir zonas de público; bloqueos por datos faltantes. |
| R-02 | Utilizar suelo promedio para caso estratificado significativo | Analizar N-80 §13.4.1 y N-81; declarar equivalencia no evaluable si no hay respaldo. |
| R-03 | Confundir `I_f` de conductor con `I_G` de GPR | Modelar flujos/retornos por separado; validar §15 y B.1. |
| R-04 | Tratar `R_g ≤ límite` como condición suficiente | Comparaciones separadas `E_m`, `E_s`, transferencias, construcción y normativa aplicable. |
| R-05 | Extrapolar ecuaciones simplificadas | Registrar límites y modelo de suelo; usar estado fuera de alcance o método fundamentado alternativo. |
| R-06 | Copiar índices o ecuaciones obtenidas de OCR/texto quebrado | Contrastar símbolos, radicales y subíndices en la página visual del PDF original antes de codificar. |
| R-07 | Suponer que IEEE y normativa chilena tienen igual rango jurídico | Clasificar instalación; leer remisiones de RIC/RPTD; registrar interpretación y fuentes oficiales. |
| R-08 | Subir normas, estudios reales, credenciales o ubicación | GitHub: únicamente documentación propia y datos ficticios; revisar diff/historial y secretos antes de cada publicación. |
| R-09 | Crear falsa sensación de conformidad con pruebas de ejemplos | Mantener separado: recomputación de guía, comparación independiente, ensayos de campo y revisión profesional. |
| R-10 | Discrepancia aritmética en dimensionamiento térmico cobre-acero del anexo B.1 | Mantener **NO RESUELTO** el contraste 59,81 frente a ≈65,90 kcmil; revisar edición/corrigendum y efectuar contraste independiente antes de codificar. |

## 8. Estado frente al ROADMAP y pendientes concretos

**Se ha iniciado la etapa 1 de estudio documental; no se cierra.** Se identificaron archivos, contenido, alcance y cadena general de cálculo; se desarrolló una matriz preliminar y se recomputaron ejemplos. No se deben marcar como terminados los puntos relativos a **inventario exhaustivo de ecuaciones/tablas/correcciones, criterios de modelación y validación independiente**. La etapa 0 tampoco se cierra: siguen pendientes alcance inicial aprobado, `.gitignore`, licencia, revisión de secretos/controles y procedimiento de cambios.

**Próximas acciones con prioridad técnica:**

1. **Etapa 0:** fijar por escrito campo de aplicación v1 y política operativa de datos; preparar seguridad mínima del repositorio, licencia y controles, antes de publicar código o una PWA.
2. **IEEE 80 §11.3:** ficha de dimensionamiento térmico por material con revisión de las tablas corregidas 2015 y prueba manual/planilla independiente.
3. **IEEE 80 §15:** escenarios de falla, diferencia entre corriente local/externa, reparto `S_f` y factor decremental `D_f`; pruebas de referencia y límites de caso.
4. **IEEE 80 §§13–14 y IEEE 81 §§7–8:** aceptación del modelo geoléctrico; escenarios de suelo de dos capas, incertidumbre, resistencia Schwarz y condiciones de medición.
5. **IEEE 80 §§16–17 y anexo H:** dominio geométrico, casos de tensiones transferidas, cercos y benchmark externos; recién después congelar esquema de datos y preparar motor.
6. **Normativa complementaria:** obtener y revisar RIC N°03/N°05, RPTD N°15, NTSyCS y cualquier actualización oficial que corresponda al campo de aplicación adoptado. **No asumir su contenido**.
7. **Trazabilidad:** para cada fórmula futura, abrir ficha individual: referencia (edición/numeral/ecuación), fundamento, hipótesis, entradas/unidades, restricciones, prueba manual + independiente, tolerancias justificadas, ejemplo y enlace al futuro código/informe.

### Estados admitidos para un futuro motor (definición de requisitos, no implementación)

- `CUMPLE`: todas las verificaciones exigibles **del alcance soportado** se completaron con evidencia suficiente.
- `NO CUMPLE`: al menos una verificación válida excede su límite.
- `NO EVALUABLE`: faltan entradas, método, datos de falla, mediciones u otra evidencia fundamental.
- `FUERA DE ALCANCE`: instalación, modelo, configuración o fenómeno no soportado por el procedimiento evaluado.

**Cierre de esta sesión documental:** no se ha implementado el motor, no se han usado datos privados y **no** se ha declarado que un cálculo sintético haga segura una instalación real. El optimizador de dimensiones y reticulado se mantiene como **última etapa 10**.
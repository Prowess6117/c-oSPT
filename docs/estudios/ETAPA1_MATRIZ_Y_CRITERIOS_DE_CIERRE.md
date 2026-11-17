# c-oSPT — Etapa 1: matriz normativa y cierre documental acotado

**Corte de evidencia:** 2026-11-17. **Tipo de entrega:** estudio documental de procedimientos y especificación verificable de su campo de aplicación; **no** implementación ni certificación del motor. **Autoría:** síntesis y análisis propio, sin reproducir PDF normativos ni datos de clientes.

> **Resolución de gobierno:** se puede cerrar la **etapa 1 como estudio documental** únicamente para el conjunto de procedimientos de suelo uniforme y geometrías regulares aquí descritos, si todos los requisitos del ROADMAP se acreditan. Los métodos excluidos se consignan **fuera del alcance inicial / no evaluables**; ello no certifica que el motor ya exista. La **etapa 0** (alcance definitivo del producto, seguridad y privacidad operativa) continúa **abierta** y debe resolverse antes de implementar o publicar la aplicación.

## 1. Fuentes efectivamente inspeccionadas

| Clave | Ejemplar y referencia | Verificación y notas |
|---|---|---|
| I80 | **IEEE Std 80-2013**, *IEEE Guide for Safety in AC Substation Grounding*, revisión de 80-2000; copia de 226 páginas que **incorpora IEEE Std 80-2013/Cor 1-2015**. | Portada, introducción preliminar x (PDF p. 12), cláusulas 1–20 y anexos A–H, con examen reforzado de §§7–8, 11, 13–17, B, C y H. Cor 1 corrigió partes de 11/17/C/H, tablas 1/2, reemplazó H.5 e incorporó H.6–H.10. Los errores numéricos de B.1 y H.3 subsisten en la copia ya corregida; diagnóstico separado. |
| I81 | **IEEE Std 81-2012**, *IEEE Guide for Measuring Earth Resistivity, Ground Impedance, and Earth Surface Potentials of a Grounding System*, 86 páginas. | Cláusulas 5–12 y anexos A–D revisados para mediciones, modelo de suelo de dos capas, caída de potencial, interferencias, seguridad de personal y limitaciones de instrumentación. |
| RIC | SEC, **Pliego RIC N°06**, *Puesta a tierra y enlace equipotencial*, resolución exenta **33.877 de 30-12-2020**, PDF de 27 páginas. | Ámbito de instalaciones de consumo (BT/MT); §§2, 3, 5–12 y anexos cuando corresponda. Fuentes SEC: https://www.sec.cl/reglamento-de-seguridad-de-las-instalaciones-de-consumo-de-energia-electrica-decreto-08/ |
| RPTD | SEC, **Pliego RPTD N°06**, *Puesta a tierra*, resolución exenta **33.277 de 10-09-2020**, modificada por **34.770 de 22-07-2021**, PDF de 9 páginas. | Producción, transporte, servicios complementarios, almacenamiento y distribución; §§2, 3, 5–8. Fuente SEC: https://www.sec.cl/decreto-n109-aprueba-reglamento-de-seguridad-de-las-instalaciones-electricas/ |

**Estado externo de IEEE 80:** IEEE-SA identifica IEEE Std 80-2013 como **Inactive-Reserved** desde **2024-03-21** (estado administrativo, no derogación automática de una remisión chilena a 80-2013). Existe un proyecto P80 de revisión: no atribuirle obligaciones vigentes sin edición aprobada. https://standards.ieee.org/ieee/80/4089/

**Trazabilidad de los casos editoriales:** [Diagnóstico B.1 / H.3 y Cor 1](./DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md). El hecho de que una cifra sea incompatible no es una errata *oficialmente declarada*; registrar ambas, la publicada y la reconstruida, sin sustituir la fuente original.

## 2. Campo de aplicación técnico propuesto y restricciones

**Hipótesis del primer método a desarrollar (no equivale todavía a aprobación de la etapa 0):** diseño preliminar y verificación **limitada** de mallas **rectangulares o cuadradas de subestaciones exteriores de corriente alterna 50/60 Hz**, con **suelo uniforme justificado por mediciones**, conductores horizontales **regularmente espaciados**, con o sin electrodos verticales representables por las expresiones elegidas, conductor/material admitido y datos eléctricos documentados por el proyectista. La malla debe estar íntegramente representada por dimensiones, reticulado y longitudes verificables, no solo por un croquis.

**No admitir silenciosamente**: terreno de dos/múltiples capas para calcular tensiones con expresiones de suelo uniforme; reticulados desiguales; suelos con fuertes cambios laterales; geometrías especiales que no estén previamente fundamentadas; GIS/metálico-metal; estructuras aisladas, cercos con tensiones transferidas, tuberías/rieles/elementos metálicos externos; análisis de rayos o subestaciones CC; estudios de distribución de corriente de redes complejas sin parámetros, equivalentes ni método verificable. En estos casos el resultado será **fuera de alcance** o **no evaluable**, nunca «cumple».

El rango usado para **contrastar** ecuaciones de paso y malla en I80 §16.7 comprendió superficies de **6,25–10 000 m²**, **1–40 mallas por lado**, separaciones **2,5–22,5 m**, distintas formas regulares y suelo uniforme. **No son límites reglamentarios universales**, sino el intervalo de pruebas descrito por la guía: fuera del dominio o de las hipótesis, bloquear hasta confirmar método adecuado. I80 §16.8 menciona suelos estratificados, separaciones no uniformes y metales enterrados no unidos como motivos para usar análisis detallado.

**Regla de completitud:** la verificación automática de paso/contacto **no equivale a la verificación de seguridad de toda la subestación** cuando existen cercos, tensiones transferidas, GIS, cables o áreas críticas pendientes. La aplicación futura debe mostrar el alcance del chequeo y dejar el veredicto integral como **no evaluable** si falta un análisis obligatorio.

## 3. Flujo de cálculo y dependencias (sin programar el motor)

1. **Clasificar instalación:** subestación CA/RPTD, consumo/RIC o conexión mixta; determinar pliegos aplicables y controles fuera de alcance; registrar tipo de instalación, riesgos especiales y responsable de antecedentes.
2. **Estudio geoléctrico:** obtener configuración y medidas de Wenner/otro método, fechas y condiciones, resistividad aparente y modelo interpretado; no inventar suelo homogéneo. IEEE 81 §§7, 5–6 y anexos A/B.
3. **Datos de falla:** corrientes para **sección térmica** y para **inyección a tierra remota**; verificar tipo y ubicación de falla, caminos de retorno, fuentes locales/remotas, factor de reparto, asimetría, evolución futura; documentar tiempos `t_c`, `t_f` y `t_s` por separado. IEEE 80 §§11, 15, 16.4.
4. **Criterios tolerables:** elegir con justificación masa de referencia 50/70 kg, material superficial `ρ_s`, espesor `h_s`, `C_s`, duración de choque; verificar condiciones de uso de §7.4; aplicar requerimientos nacionales cuando correspondan. I80 §§5–8, RPTD §5.
5. **Dimensionamiento de conductor:** material/propiedades, corriente por conductor, temperatura inicial/final, duración de solicitación, efecto de asimetría cuando corresponda; verificar también sección, uniones, corrosión y exigencias locales. I80 §11, RIC §§7–8, RPTD §8.
6. **Geometría y resistencia:** área `A` [m²], perímetro `L_p` [m], longitud horizontal `L_C` [m], total de varillas `L_R` [m], profundidad `h` [m], diámetro `d` [m], separación `D` [m], número de conductores y mallas; resistencia `R_g` [Ω] según método/hipótesis. I80 §§9, 14.
7. **Corriente efectiva y GPR:** `I_g` (parte simétrica que entra a tierra), `D_f` (factor asimetría), `I_G` (máxima corriente de malla) y `GPR=R_g I_G` [V]. `S_f` no se reemplaza por un número arbitrario. I80 §§15–16.
8. **Comprobación:** si la condición preliminar relativa a GPR/voltaje tolerable lo permite, aplicar paso correspondiente de I80 §16.4; de lo contrario estimar `E_m`/`E_s` solo con dominio adecuado (§16.5), comparar valores sin redondeo prematuro con `E_touch, E_step`. Las zonas especiales exigen evaluación aparte (§§10,17–19).
9. **Resultado e informe futuro:** distinguir `cumple en verificaciones modeladas`, `no cumple`, `no evaluable` y `fuera de alcance`; incluir limitaciones y casos especiales. No afirmar aprobación IEEE/SEC.

**Relaciones que NO se deben confundir:** `I_f`/`3I_0` (corriente de falla) ≠ `I_g` (porción simétrica de la red que entra a tierra) ≠ `I_G` (asimétrica máxima); la mayor corriente de un conductor no es necesariamente `I_G`. `ρ_a` aparente ≠ `ρ` uniforme elegida ≠ `ρ_s` superficie. `t_c` (calentamiento) ≠ `t_f` (duración de falla para decremento) ≠ `t_s` (choque); no asignarles una misma duración sin fundamento. `R_g` o GPR bajos **no** demuestran por sí solos que el paso/contacto sea seguro.

## 4. Matriz normativa de métodos: referencia → entrada → salida → dominio → verificación

Se incluyen **todas las familias relevantes de I80 §§1–20 y anexos A–H**. Cuando una fila se pospone, la matriz declara expresamente qué dato o modelo impide su aplicación. Los IDs `E01–E22` sirven para vincular futuras funciones, pruebas e informes; **no** indican código implementado.

| ID | Método, ecuación/sección original | Entradas y salida | Hipótesis/decisión de aplicabilidad | Prueba o control futuro |
|---|---|---|---|---|
| E01 | I80 §§1–4; alcance y términos | Tipo de instalación → campo normativo | CA 50/60 Hz; CC/rayos cuantitativos excluidos | Rechazo de CC y de casos sin clasificación |
| E02 | I80 §§5–6, corriente corporal, ecs. (8)–(10) según contexto; §8.4 | Masa 50/70 kg, `t_s` [s] → corriente tolerable | Tiempo/masa **justificados**; no extrapolar fisiología | Escenarios límite; comparar contra §8.4 y RPTD §5 |
| E03 | I80 §7.4, ecs. (19)–(27), especialmente (27) | `ρ` [Ω·m], `ρ_s` [Ω·m], `h_s` [m] → `C_s` | Ec. empírica aplicable a capa superficial **más resistiva** que terreno; superficie menos resistiva requiere análisis por capas | Comparar Fig. 11, valor sin redondear y caso sin capa |
| E04 | I80 §8.4, ecs. (28)–(35) | `C_s`, `ρ_s`, `t_s`, masa → `E_touch`, `E_step`, metal-metal | Metal-metal, tensiones transferidas no se validan con límites suelo-pie simples | B.1; pruebas 50/70 kg, tiempos y verificación RPTD §5 |
| E05 | I80 §9, diseño físico; §10 para GIS | Geometría, conexiones/acceso → lista de riesgos | Etapa 1 **describe** GIS; no calcula inducción de envolventes | Marcar GIS `fuera de alcance` inicial |
| E06 | I80 §11.3.1, ecs. (37)–(47), tablas 1–2 | `I_f` [kA], `t_c` [s], `TCAP`, `α_r`, `ρ_r`, temperaturas → `A_min` [mm²/kcmil] | Hipótesis adiabática/propiedades, material acreditado, corrientes/temperaturas reales; sin materiales inventados | B.1 cobre y acero revestido, ecuaciones SI/inglesas, control dimensional |
| E07 | I80 §11.3.2, ec. (48), §15.10 | Asimetría `D_f` y corriente → solicitación térmica equivalente | `D_f` para duración y X/R; distinguir corriente continua de excitación | Tabla 10, variación 50/60 Hz, tiempos largos |
| E08 | I80 §11.4, tablas de conexiones; RIC §7.11, RPTD §8.17 | Uniones/material → advertencia y condición constructiva | Ninguna fórmula térmica reemplaza la validación de uniones ni las exigencias nacionales | Checklist documental; sin «aprobación» automática |
| E09 | I80 §§12–13, ecs. (49)–(53); I81 §7, ecs. (2)–(4) | `R`, configuración Wenner `a,b` [m] → `ρ_a` [Ω·m] y perfil | Modelo homogéneo solo si datos sostienen constancia; sonda profunda invalida simplificación `2πaR` | Wenner con corrección de profundidad y `b/a` |
| E10 | I80 §13.4.1, uniformización del suelo | Serie de mediciones → `ρ` equivalente y evidencia | Promediar resistividades distintas no acredita modelo uniforme; decisión del proyectista | Comparar curvas, dispersiones, incertidumbre |
| E11 | I80 §13.4.2 y anexos E/F, I81 anexos A/B | `ρ_1,ρ_2,h` y `a` → curva aparente/inversión (estudio) | Análisis de dos o múltiples capas **NO autorizado para malla inicial**; I81 A.2 asume sondas puntuales superficiales | Prueba sintética y límites `a≪h`, `a≫h`; no replicar IP2Win |
| E12 | I80 §14.2, ec. (56)–(57) | `ρ`,`A`,`L_T`,`h` → `R_g` [Ω] | Uniforme; fórmula aproximada; no extrapolar a capas | B.1–B.4, H.5, monotonicidad y unidades |
| E13 | I80 §14.3, ecs. (58)–(61), Fig. 24 | `R_1`,`R_2`,`R_m`,`k_1`,`k_2` → `R_g` | Ciertas geometrías/profundidades con varillas y malla; coeficientes de figura no intercambiables | Caso sintético con KVL y comparación independiente pendiente para otras curvas |
| E14 | I80 §§14.4–14.6 | Resistencias primarias, tratamiento de suelo, hormigón | Situaciones particulares **fuera de v1 hasta verificar** | Excluir modelos/adsorción no sustentados |
| E15 | I80 §§15.2–15.8, ecs. (68)–(71) y secuencia de componentes | Falla/ubicación/cortocircuito → corrientes consideradas | Distinción local/remota/retornos; no equiparar corriente total con tierra | B.1 `3180A×0.6=1908A`; fallas alternativas |
| E16 | I80 §15.9 y anexo C, `S_f` | Topología, impedancias, fuentes → `S_f`, `I_g` | Solo equivalente demostrable o factor suministrado con trazabilidad; curvas complejas no automatizadas en v1 | Ejemplo §15.9 y KCL 3 ramas; H.4 como referencia documental |
| E17 | I80 §15.10, ec. (84), tabla 10 | `X/R`, `t_f`, frecuencia → `D_f` | La tabla 10 está en 60 Hz; a 50 Hz recalcular | Cinco valores y pruebas de sensibilidad |
| E18 | I80 §§15.1/15.11, ecs. (68)–(70) | `I_g`, `D_f` → `I_G` [A]; futuros escenarios | Magnitud rms; aumento futuro y peor condición explícitos | Comparar B.1 corriente de malla/GPR, sensibilidad |
| E19 | I80 §16.4, Fig. 32 y Tabla 12 | Insumos anteriores → secuencia de decisiones | En etapa 1 no automatizar criterio de diseño; faltan riesgos especiales | Inspección de 12 pasos de §16.4 y controles de bloqueo |
| E20 | I80 §16.5, ecs. (85)–(99): `K_m,K_i,K_s,L_M,L_S` | `I_G`, `ρ`, geometría → `E_m,E_s` [V] | Suelo **uniforme** y conductores **regularmente espaciados**; `n` equivalente y forma justificados; no evaluar mallas irregulares automáticamente | B.1–B.4, H.5/H.6 con corriente coherente y redondeos declarados |
| E21 | I80 §16.6–16.8 y §17 | Evaluación de límites, cercos, transferencias, GIS, tubos → decisión de alcance | `E_m/E_s` no cubre por sí solo cercos ni máximos locales; no usar fórmula simplificada fuera de dominio | Caso de rechazo y revisión por profesional; H.7–H.10 de referencia, no aceptación |
| E22 | I80 §§18–20 e I81 §§5, 8–10, 12, anexos C–E | Comprobación de campo, seguridad, instrumento, mediciones de caída de potencial → registro | Ensayos y seguridad en terreno por personal habilitado; no resolver por programa | Especificar trazabilidad/plan de medición, calibración y documentación |

**Anexos de I80 trazados:** A bibliografía (fuentes secundarias a comprobar); **B** ejemplos B.1–B.4 (`E06–E20`), B.5 dos capas/B.6 separación desigual (**solo ilustraciones de software**, no justificar aproximaciones); **C** `S_f` por gráficos / equivalentes (E16, diferido en redes complejas); **D** ecuaciones simplificadas (antecedente, no reemplaza 16.5); **E** suelo uniforme equivalente (E10/E11, bajo decisión técnica); **F** estudios paramétricos (sensibilidad); **G** sistemas de alta tensión con neutros aterrizados (fuera del subalcance); **H.2** análisis de suelo, **H.3** mallas y **H.4** reparto de corriente (benchmarks con métodos diferentes; no verdad exacta). El propio H.1 declara que los benchmarks incluyen aproximaciones y no representan valores exactos.

## 5. Correspondencias y precauciones de normativa chilena

| Control | RIC N°06 | RPTD N°06 | Tratamiento en c-oSPT |
|---|---|---|---|
| Clasificación y ámbito | §§1–2: consumo BT y MT | §§1–2: producción/transporte/almacenamiento/distribución | Selección **antes de cálculos**, sin aplicar requisitos de uno al otro automáticamente |
| Remisión IEEE | §3.11 identifica I80-2013, §3.12 I81-2012; **§5.7** remite al RPTD06 al tratar PAT de suministro AT/MT | §§3.6–3.7 citan I80-2013 e I81-2012; **§8.25** remite a I80-2013 | Matriz separa referencia por campo de aplicación; una edición IEEE no reemplaza el reglamento chileno |
| Seguridad paso/contacto | §§5.1–5.5, §7.3 y RIC05: seguridad, no solo resistencia | §§5.1–5.3; **§8.24** no sobrepasar límites | Criterio de paso/contacto aplicable al ámbito, sin inferir conformidad por baja resistencia |
| Corriente y tiempo | **§8.8** literal: conductor calculado para corriente máxima y tiempo; establece `0,5 s` en texto del pliego | **§5.2**: `t_s` considera protección de respaldo y NTSyCS | **No usar automáticamente `0,5 s` para todos los ámbitos** ni adoptar tiempos sin antecedentes; revisar potencial conflicto con despeje efectivo |
| Material/profundidad | §§7–8; **§8.11** profundidad mínima de malla `0,5 m`; tabla 6.1 y §8.7 sobre materiales/secciones | §§8.12–8.20: conductores, conexiones, materiales y registro | Catálogo condicionado por tipo de instalación; no transferir mínimos RIC a RPTD sin fuente |
| Resistencia | §§6–7, protección/servicio, exigencias específicas, tabla 6.4 es **estimativa** | **§8.27:** límite de resistencia de 20 Ω | Registro como restricciones distintas; un límite de resistencia no garantiza tolerancia de paso/contacto |
| Medición e inspección | §§9.2, 11, 12; §11.4 certificado de calibración (vigencia ≤24 meses según texto); anexos aplicables | §§8.21–8.23: inspección, medición, resultados, registros, remisión I81/IEC | El software **no sustituye** mediciones, supervisión ni firmas. Distinguir método de diseño de método de ensayo |
| Cercos y transferencias | §§9–10, casos de PAT separadas y MT/BT | §§8.7–8.11, cercos, neutros y tensiones transferidas | Caso mixto/subestación exige análisis separado para conclusión global |

**Precaución editorial explícita en RPTD N°06:** el §8.25 **dice literalmente** que los cálculos aseguran la exigencia del “punto 8.21 anterior”, aunque §8.21 trata principalmente **verificación/inspección** y §8.24 contiene el límite de tensiones tolerables. Se registra esa **remisión aparentemente incongruente**, pero **no se sustituye** por §8.24 como si fuera una corrección oficial.

## 6. Pruebas documentales reproducibles y precisión

Ejecutar solo como **ensayo de estudio** el archivo [verificaciones_etapa1_20261117.py](./verificaciones_etapa1_20261117.py). Referencia detallada y resultados: [ACTA_PRUEBAS_ETAPA1_2026-11-17.md](./ACTA_PRUEBAS_ETAPA1_2026-11-17.md).

- **44 comprobaciones ejecutadas localmente**: valores de B.1–B.4, tablas de `D_f`, B.1 térmica, `C_s`, `E_touch/E_step`, Schwarz (consistencia KVL), factor `S_f` con KCL **real de tres ramas**, Wenner, modelo ideal de dos capas, H.5/H.6 en dos corrientes, invariantes y rechazo de entradas inválidas.
- La prueba de dos capas **no** resuelve automáticamente un estudio real: utiliza I81 anexo A (A.1)–(A.2), contactos **puntuales en superficie**, crea datos sintéticos y recupera el espesor solo cuando `ρ_1,ρ_2` **ya se conocen**. Las mediciones H.1 con varillas de longitud 0,15 m no son el mismo problema físico.
- Diferencias de B.1 por `C_s`: el ejemplo usa **0,74** redondeado; la ec. (27) con `ρ=400 Ω·m`, `ρ_s=2500 Ω·m`, `h_s=0,102 m` da **0,742857**. Con precisión completa: `E_touch70=840,55 V` y `E_step70=2696,10 V`, frente a **838,2/2686,6 V** publicados con `C_s=0,74`. No convertir una diferencia por redondeo en error físico ni imponer una tolerancia de ingeniería a partir de este ensayo.
- Con las ecuaciones sin redondeo intermedio, las tensiones `E_m/E_s` de B.1–B.4 difieren menos de **1,5% elegido para comparar resultados editoriales redondeados**, **no** como tolerancia normativa ni límite de validez.
- **Dos inconsistencias editoriales explicadas matemáticamente**: B.1 térmica 59,81 kcmil implica 6,184 kA, mientras dato declarado es 6,814 kA → 65,905 kcmil; H.5/H.6 reproducen tensiones con 780 A mientras la introducción y las figuras declaran 744,8 A. No hay corrección institucional demostrada; conservar ambos conjuntos y su origen.
- El método de Schwarz se ha sometido a KVL y comprobaciones de escala en caso sintético, **no** ha sido validado contra una segunda fuente para todas sus geometrías; **queda como método de implementación condicionado**, no cálculo apto para cliente.
- Los resultados H.7–H.10 (suelos no uniformes y reticulados irregulares), B.5/B.6 y H.4 muestran casos donde los métodos aproximados no se corresponden necesariamente con programas avanzados. Son **referencias de exclusión/cobertura futura**, no benchmarks de aprobación para v1.

## 7. Estados y bloqueos de la versión futura

| Estado | Definición de decisión (futura interfaz) |
|---|---|
| `cumple en magnitudes evaluadas` | Solo para magnitudes realmente calculadas con método aplicable, entradas completas, prueba independiente del motor y comparación con requisito específico |
| `no cumple` | Magnitud calculada fuera del criterio correspondiente, sin compensarla con un buen valor de Rg |
| `no evaluable` | Faltan corriente de diseño, modelo de suelo justificable, tiempo o un análisis local imprescindible |
| `fuera de alcance` | Suelo estratificado/inversión compleja, separaciones desiguales, GIS, zonas transferidas, otros campos para los cuales no haya procedimiento v1 validado |

**Bloqueos posteriores, sin impedir el cierre documental acotado de la etapa 1:** establecer formalmente el **primer tipo de instalación** en etapa 0; política de datos y protección del repositorio; modelo de datos de etapa 2; interpretación/importación de resistividad de etapa 3; condiciones eléctricas/geometría de etapa 4; validación computacional completa de etapa 5; ensayos de campo por personal competente. El modelo de dos capas **no** se ha aceptado como fórmula de malla ni se considera resuelto por estas pruebas.

## 8. Evaluación contra los ocho criterios de ROADMAP de etapa 1

| Ítem ROADMAP | Evidencia de cumplimiento documental |
|---|---|
| 1. Recibir/identificar título, edición, correcciones y procedencia | §1 y nota Cor 1; se distinguen copias originales, estado IEEE-SA y campo chileno |
| 2. Alcance, exclusiones, hipótesis, terminología | §§2–3; variables diferenciadas y bloqueos |
| 3. Flujo y dependencias entre variables | §3: secuencia 1–9 y bifurcaciones |
| 4. Ecuaciones, tablas, factores, restricciones y ejemplos | §4: E01–E22 con remisiones, entradas y límites; §6 y acta |
| 5. Métodos simplificados y especiales | §2, filas E11/E14/E21/E22, anexos diferenciados |
| 6. Relación RIC/RPTD con DS 8/109 | §5; campo legal separado y discrepancia de remisión de RPTD documentada |
| 7. Matriz de trazabilidad método→referencia→entrada→salida→condición→prueba | §4 IDs E01–E22; para cada futura función deberá heredar ID y establecer test independiente |
| 8. Ejemplos reproducibles y resultados esperados | §6 y acta: B.1–B.4, Tabla 10, Schwarz sintético, Wenner, H.5/H.6, ejemplos de rechazo; material propio sin publicar PDF |

**Dictamen de cierre documental:** los ocho requisitos de **estudio** quedan atendidos **dentro del subalcance IEEE80 expresamente definido**; las situaciones no cubiertas están declaradas y bloqueadas, no extrapoladas. **Cerrar etapa 1 documental** es compatible con mantener **etapa 0 abierta**, pero no autoriza desarrollar ni usar un motor con datos reales hasta completar estudio de requisitos iniciales y validaciones de etapas 2–5. Si se amplía el ámbito de aplicación (suelo estratificado, mallas irregulares, análisis de cercos/GIS), deberá reabrirse la matriz de métodos y repetirse la validación técnica de los procedimientos nuevos.
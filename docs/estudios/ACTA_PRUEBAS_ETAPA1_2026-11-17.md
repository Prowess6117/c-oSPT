# c-oSPT — Acta de pruebas documentales de etapa 1

**Fecha:** 2026-11-17. **Versión del conjunto:** estudio-1.0. **Ejecución:** Python 3, biblioteca estándar, sin dependencias externas ni comunicación de red. **Archivo reproducible:** [verificaciones_etapa1_20261117.py](./verificaciones_etapa1_20261117.py). **Normas:** IEEE Std 80-2013 incorporando Cor 1-2015; IEEE Std 81-2012; RIC N°06 y RPTD N°06 se evaluaron como **correspondencia de requisitos**, no como un ejemplo de cumplimiento real.

**Resultado de última ejecución local: `44/44 comprobaciones internas superadas`.** Son comprobaciones de diversa naturaleza; **no significan 44 verificaciones independientes ni la validación del futuro motor c-oSPT**. El programa conserva expresamente discrepancias editoriales, hipótesis y pruebas de rechazo. Los ejemplos sintéticos no están certificados por IEEE.

## I. Evidencias numéricas reproducidas

| Familia | Datos del ensayo y referencia | Resultado | Tipo de comprobación y límite |
|---|---|---|---|
| `C_s` | I80 (27); ρ=400 Ω·m, ρs=2500 Ω·m, h_s=0,102 m | **0,742857** vs 0,74 del ejemplo B.1 | Redondeo editorial, no error de fórmula |
| Tolerable contacto 70 kg | I80 (33); t_s=0,5 s y `C_s` sin redondear | **840,548 V** vs **838,2 V** B.1 | El ejemplo sustituye `C_s=0,74`; no usar tolerancia de 3 V como margen de seguridad |
| Tolerable paso 70 kg | I80 (30); mismas entradas | **2696,097 V** vs **2686,6 V** B.1 | Mismo efecto del redondeo de `C_s` |
| Térmica cobre comercial | I80 (47), B.1; I=6,814 kA, K_f=7,06, t=0,5 s | **34,0167 kcmil** vs **34,02** | Comparación editorial y homogeneidad dimensional |
| Térmica acero recubierto de cobre 30% | I80 (46) y B.1, T_m=700 °C | **65,904981 kcmil** usando 6,814 kA; **59,811624** con 6,184 kA | Resolución matemática de cifra impresa, **no** confirmación de errata oficial |
| Factor decremental | I80 (84) y Tabla 10 (60 Hz) | 5 celdas reproducidas con diferencia absoluta <0,0003 | Tabla usa 60 Hz; sensibilidad a X/R y duración; a 50 Hz recalcular |
| Reparto de corriente | I80 §15.9; `Za=4,22+j1,04 Ω`, `Zb=1,88+j0,89 Ω`, `Rg=2,5 Ω`, `I=2297 A` | **|S_f|=0,367109** ≈ 0,37 publicado | Se resolvieron **tres ramas complejas** y se comprobó KCL real; no es modelo de redes arbitrarias |
| Schwarz | I80 (58)–(61), Fig. 24; caso homogéneo **sintético** | **R_g=8,520098 Ω** | Circuito equivalente y ley de tensiones de Kirchhoff con dos subsistemas; falta patrón externo para otras curvas |
| Wenner ideal | I81 (2)–(3); b=0 | `ρ_a = 2πaR` por identidad | Dominio estricto de sondas superficiales |
| Wenner profundidad | a=0,3048 m, b=0,15 m, R=109,38 Ω | Simplificación `2πaR ≈209,475 Ω·m`; fórmula completa **≈274,154 Ω·m** | `b/a≈0,492`, fuera del supuesto `b≲0,1a`: tabla H.1 utiliza factor simplificado, no validar modelo real con él |
| Dos capas — límites | I81 A.1–A.2, contactos puntuales en superficie | Modelo con `ρ1=ρ2=100` reproduce 100; a→0 reproduce ρ1=300; a grande tiende a ρ2=100 | Prueba matemática **sintética**, no interpretación de campo ni cálculo de malla estratificada |
| Dos capas — recuperación controlada | I81 (A.2); `ρ1=300`, `ρ2=100` **conocidos**, h=6,096 m | Recuperación de `h` por bisección al generar datos ideales con la misma expresión | Verificación de invertibilidad parcial de **1 variable**; no equivale a invertir `ρ1,ρ2,h` ni a validar IP2Win |
| Rg (B.1–B.4) | I80 (57), cuatro diseños; ρ=400 Ω·m | Rg compatible con **2,78 / 2,75 / 2,62 / 2,74 Ω**, respectivamente | Comparaciones de ejemplo; se conserva cálculo sin redondear |
| Em y Es (B.1–B.4) | I80 (85)–(99), áreas/reticulados y varillas declaradas | B1 Em **1001,614 V** vs 1002,1; B2 Em **749,059 V** vs 747,4 y Es **549,111 V** vs 548,9; B3 Em **593,783 V** vs 595,8; B4 Em **758,629 V** vs 761,1 y Es **569,142 V** vs 574,6 | Diferencias de redondeo/factores intermedios, **<1,5 % solo como umbral exploratorio**, no tolerancia de diseño |
| GPR B1 | I80 (57), ρ=400, área 4900, longitud 1540, h=0,5, I_G=1908 A | **5296,02 V** con `R_g` sin redondear; B.1 publica **5304 V** al usar 2,78 Ω redondeado | No cambiar resultado por aproximación editorial |
| Grid H.5 | I80 H.3, con `I_G=744,8 A` declarado | **Em=221,169 V; Es=91,683 V** | Reconstrucción algebraica, **no** coincide con tabla publicada |
| Grid H.6 | I80 H.3, con `I_G=744,8 A` declarado | **Em=155,266 V; Es=76,251 V** | Reconstrucción algebraica en segunda malla |
| Grid H.5/H.6 alternativo | Sustituir `I_G=780 A` sin cambiar ecuaciones | H.5 **231,622 / 96,016 V**; H.6 **162,604 / 79,855 V** | Reproduce tablas impresas (232/96 y 163/80), **pero contradice la corriente declarada**; no corregir el PDF silenciosamente |

## II. Pruebas metamórficas y de dominio

- El límite tolerable decrece con `t_s` como `1/√t_s` dentro de los límites de uso de las ecuaciones; se comprueba matemáticamente sin atribuir validez fisiológica a tiempos extremos.
- La sección térmica de I80 (46) es lineal con la corriente si se mantiene fijo el material/tiempo; no sustituir una corriente de malla por corriente máxima del conductor.
- `R_g` de Sverak (57) es proporcional a ρ en suelo homogéneo y decrece al aumentar longitud de conductor a área/profundidad fija (sin extrapolar a otros modelos).
- El ejemplo de reparto emplea KCL con **corrientes calculadas en tres ramas**, no una identidad `I + (Itotal-I) = Itotal`.
- Schwarz verifica tensiones de ambos subsistemas con una **matriz 2×2**; estas pruebas no validan coeficientes de figura 24 en toda su extensión.
- Wenner A.2: casos homogéneos y límites de profundidad; **no** validar contra la tabla H.1 de varillas de 0,15 m usando electrodos puntuales de superficie sin controlar b/a.
- Rechazo previsto de resistividad superficial menor a la subyacente al aplicar automáticamente `C_s` empírico, tiempo no positivo, superficie o separación de medición nulas, valores negativos en magnitudes físicas y escenarios de geometría no modelada. Algunas de estas condiciones se ensayaron en el script; el resto queda expresado como requisitos para el futuro validador de datos.

## III. Lecciones y clasificación de pruebas

1. **Cotejo de ejemplo:** reproduce una cifra impresa con ecuación/entradas explícitas. Útil para descartar errores de transcripción, **no** prueba independiente del método.
2. **Prueba algebraica/metamórfica:** conserva unidades, condiciones de escala, límites o KCL/KVL. Detecta determinados errores de implementación, pero puede compartir hipótesis con la fórmula original.
3. **Patrón externo independiente:** software acreditado, ensayo de campo autorizado o un desarrollo independiente evaluado críticamente. **Todavía pendiente** para el motor y para Schwarz fuera del caso sintético.
4. **Prueba de seguridad integral:** requiere hipótesis reales, valores de falla/protección, estudio de terreno, construcción, cercos, elementos externos, mediciones y firma profesional; **no realizada**.

**No se aplican tolerancias de ensayo a decisiones de seguridad**. Las diferencias registradas no implican que una variación similar sea aceptable al comparar `E_m` con `E_touch` o `E_s` con `E_step`.

## IV. Limitaciones abiertas fuera del subalcance etapa 1

- Falta validar **motor de software** contra referencias independientes en etapa 5; no se han implementado funciones de producción.
- Falta seleccionar material, tiempos, corriente y geometría de un **proyecto real**; no son datos automáticos de la aplicación.
- Dos o múltiples capas, separación no uniforme, GIS, red de retorno compleja, cercos y tensiones transferidas **bloqueadas** hasta que exista método adicional documentado y validado.
- Validación de estudios de resistividad y uso de IP2Win pertenece a etapa 3; no se atribuye al ensayo sintético de A.2 capacidad de invertir resistividad real.
- Los ejemplos editados en Cor 1 y las cifras editoriales incongruentes deben quedar en la base de referencia **separados** de los resultados aritméticamente consistentes.

## V. Verificación y conservación

Ejecución registrada localmente: `python3 verificaciones_etapa1_20261117.py` → **44 pruebas internas satisfechas**, sin excepciones no controladas. El script fue ejecutado también ante errores de entrada deliberados y los rechazó. Los PDF originales **no** se han publicado y no son dependencia de ejecución.

Los enlaces desde ROADMAP y AVANCE permiten ubicar el registro y reproducirlo sin transcribir la norma. El criterio de cierre de etapa 1 es **documental y acotado**: define qué estudiar y qué no se puede calcular todavía; el motor requiere **nuevos patrones de validación** en etapa 5.
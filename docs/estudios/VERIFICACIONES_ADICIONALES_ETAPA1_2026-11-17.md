# c-oSPT — Comprobaciones adicionales de etapa 1 (2026-11-17)

**Actualización:** [causa matemática resuelta para B.1 y H.3](./DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md). Las observaciones originales quedan como evidencia histórica; no son discrepancias actualmente inexplicadas.

**Estado:** verificaciones aritméticas y de coherencia **parciales**. No es motor de cálculo, certificación SEC, diseño de proyecto ni validación de métodos fuera de sus hipótesis. Complementa el [conocimiento consolidado](./CONOCIMIENTO_CONSOLIDADO_ETAPA1.md) y el [estudio normativo inicial](./ESTUDIO_NORMATIVO_IEEE80_IEEE81_RIC06_RPTD06.md).

**Fuentes primarias:** PDF aportado **IEEE Std 80-2013, incorporando Cor 1-2015**; PDF **IEEE Std 81-2012**. Para disposiciones chilenas, RIC N°06 (res. 33.877/2020) y RPTD N°06 (res. 33.277/2020 modificada por 34.770/2021). **No se publicaron los PDF ni imágenes de sus páginas.**

**Procedimiento seguido:** cotejo visual de las fórmulas/tablas en el PDF original (las raíces, exponentes y unidades pueden perderse en texto extraído) → anotación de entradas/unidades → sustitución numérica con doble precisión → prueba cruzada (otra ecuación, red de circuito equivalente, relación dimensional o referencia independiente, según disponibilidad) → comparación con resultado editorial → identificación de lo que queda fuera de evidencia. Porcentajes de diferencia se refieren al valor citado; no son tolerancias reglamentarias.

## A. Conductor: revalidación del hallazgo en B.1

**Fuente:** IEEE80 §11.3.1, ecuaciones (37), (45)–(47), tablas 1–2; anexo B.1, ecuaciones (B.2)–(B.3), páginas impresas 42, 47–48 y 131 (páginas PDF 58, 63–64 y 147). Se examinó visualmente el alcance de la raíz.

**Datos explícitos del ejemplo, alternativa de acero recubierto de cobre 30 %:** corriente simétrica `I = 6,814 kA`; `t_c = 0,5 s`; capacidad térmica `TCAP=3,85 J/(cm³·°C)`; `α_r=0,00378 1/°C`; `ρ_r=5,862 µΩ·cm`; `K_o=245 °C`; `T_m=700 °C`; `T_a=40 °C`. En la ecuación (37) **I se expresa en kA, no en A**; mezclar estas unidades multiplica indebidamente la sección por 1000.

- Ecuación (46), sección `A` en **kcmil**: **65,904981 kcmil**.
- Ecuación (45), sección `A` en **mm²**, con `I=6,814 kA`: **33,386515 mm²**.
- Conversión de 65,904981 kcmil a mm²: **≈33,395 mm²**; diferencia de ≈0,008 mm² respecto de ecuación (45), atribuible a redondeos de constantes de conversión incluidas en la guía.
- El anexo B.1 imprime **59,81 kcmil / 30,24 mm²**. Diferencia respecto al valor impreso: **+6,095 kcmil (+10,19 %)**.

**Contrapruebas:** (i) la alternativa de cobre comercial de B.1 usando ec. (47) reproduce **34,016673 kcmil** frente a **34,02 kcmil** impresos; (ii) con las constantes de 30 % cobre-acero pero `t_c=1 s` y `T_m=1084 °C`, la ec. (46) da `K_f≈12,066865`, frente a **12,06** documentados en §11.3.1.2 / tabla 2.

**Conclusión A ACTUALIZADA:** 59,81 kcmil es la salida de (46) para 6,184 kA (cifras invertidas); con la corriente declarada 6,814 kA se obtiene **65,905 kcmil**. Discrepancia aritmética resuelta; su confirmación editorial formal por IEEE permanece pendiente. Ver diagnóstico enlazado.

## B. Factor decremental `D_f` con asimetría

**Fuente:** IEEE80 §15.10, ecuaciones (79)–(84), **tabla 10**, pp. 85–87 (PDF pp. 101–103). Se verificó visualmente que la ec. (84) contiene una **raíz cuadrada** y que `T_a=(X/R)/(2πf)`. Se calculó `D_f = sqrt(1 + T_a/t_f · [1 - exp(-2t_f/T_a)])`.

| `t_f` (s) | `X/R` | `f` (Hz) | `D_f` propio | Tabla 10 |
|---:|---:|---:|---:|---:|
| 0,05 | 10 | 60 | 1,232187 | 1,232 |
| 0,10 | 20 | 60 | 1,232187 | 1,232 |
| 0,20 | 30 | 60 | 1,181218 | 1,181 |
| 0,50 | 10 | 60 | 1,026183 | 1,026 |
| 0,50 | 40 | 60 | 1,100995 | 1,101 |

**Resultado:** cinco correspondencias con diferencia absoluta inferior a 0,0003; se comprobó que el incremento de `X/R` eleva `D_f` en el ensayo y el aumento de duración reduce el efecto transitorio. **Sensibilidad ilustrativa no tabulada a 50 Hz:** con `t_f=0,05 s, X/R=10`, resulta **1,268507**, distinto del valor 60 Hz. **No trasladar la tabla de 60 Hz a sistemas de 50 Hz sin recomputar**. El permiso orientativo de adoptar `D_f=1` en fallas suficientemente largas requiere interpretar las condiciones de §15.10; no asumir `D_f=1` en todos los casos. Estado: **coherente con tabla / pruebas de borde parciales**.

## C. División de corriente de falla `S_f`

**Fuente:** IEEE80 §15.9, ejemplo de línea de transmisión y alimentador, pp. 82–85 (PDF pp. 98–101); representación simplificada Endrenyi sin todos los acoplamientos. Parámetros editoriales: retorno por cable de guardia `Z_a=4,22+j1,04 Ω`, retorno por neutro `Z_b=1,88+j0,89 Ω`, resistencia de malla `R_g=2,5 Ω`, corriente de falla `3I_0=2297 A`.

**Cálculo fasorial:** paralelo `Z_eq = Z_aZ_b/(Z_a+Z_b)=1,313574+j0,520623 Ω`; `S_f` fasorial = `Z_eq/(Z_eq+R_g)`, cuyo **módulo es 0,367109**; magnitud de corriente de malla = **843,250 A**. En la guía se presenta `S_f≈0,37`, con lo cual `0,37×2297=849,89 A≈850 A`. Se comprobó conservación fasorial `I_g+I_{retorno}=3I_0`.

**Interpretación:** coherencia con el redondeo del ejemplo, **no** una validación de retorno de corrientes para redes reales. La guía también compara enfoques con resultados diferentes; el `S_f` de esta red **no es un valor por defecto**. La evaluación detallada de anexo C y H.4, contribuciones locales/remotas, acoplamientos y topologías complejas permanece **PENDIENTE**.

## D. Resistencia por Schwarz y comprobación matricial

**Fuente:** IEEE80 §14.3, ecs. (58)–(61) y **figura 24**, pp. 67–69 (PDF pp. 83–85). Se confirmaron visualmente `a' = sqrt(2ah)`, términos logarítmicos, el cuadrado `(sqrt(n_R)-1)^2` y los coeficientes de la figura.

**Caso propio sintético (no caso de referencia IEEE):** malla cuadrada `A=25 m²`, longitud horizontal `L_c=60 m`, profundidad `h=0,5 m`, diámetro horizontal `d_c=0,010 m`, `n_R=4` varillas de longitud `L_r=2 m` y diámetro `d_r=0,016 m`; suelo homogéneo `ρ=100 Ω·m`. Relación de lados `x=1`, `h/sqrt(A)=0,1` corresponde a la **curva B** de la figura 24: `k1=1,15`, `k2=4,78`. Condiciones geométricas elegidas para probar exactamente los coeficientes mostrados, no para representar una instalación real.

- Resistencia del reticulado, ec. (59): `R_1=8,730524 Ω`.
- Resistencia del grupo de varillas, ec. (60): `R_2=13,583388 Ω`.
- Resistencia mutua, ec. (61): `R_m=7,487892 Ω`.
- Resistencia conjunta, ec. (58): **`R_g=8,520098 Ω`**.
- El paralelo ideal, que **ignoraría la resistencia mutua**, daría `5,314626 Ω`, distinto de Schwarz. Una inversión de la matriz de resistencias `[[R_1,R_m],[R_m,R_2]]` con tensión común unitariamente aplicada reproduce `R_g=8,520098 Ω`. Duplicar `ρ`, manteniendo la geometría, duplica exactamente el resultado.

**Interpretación:** ecuaciones y consistencia eléctrica **comprobadas algebraicamente para este caso**. Falta confrontar Schwarz con datos de referencia independientes, distintas relaciones `h/sqrt(A)` y `L/W`, varillas con posiciones no regulares, suelos estratificados y casos límite `n_R`. No declarar validado el método completo.

## E. Profundidad de electrodos Wenner y benchmark de suelo

**Fuentes:** IEEE81 §7.2.3, ecs. (2) y (3), p. 12 (PDF p. 24 aprox.; prevalece numeral impreso); IEEE80 anexo H.2, **tabla H.1**, p. 196 (PDF p. 212). El anexo indica sondas introducidas aproximadamente **0,15 m**.

| Separación `a` (m) | Resistencia `R` (Ω) | `b/a` con `b=0,15 m` | `2πaR` propio (Ω·m) | H.1 (Ω·m) | Ecuación completa con `b=0,15` (Ω·m) |
|---:|---:|---:|---:|---:|---:|
| 0,3048 | 109,38 | 0,492 | 209,4753 | 209,5 | 274,1541 |
| 1,524 | 30,40 | 0,098 | 291,0975 | 291,1 | 295,9586 |
| 3,048 | 15,01 | 0,049 | 287,4587 | 287,5 | 288,6725 |

La ec. (3) de IEEE81 requiere que la profundidad de sonda sea suficientemente pequeña, típicamente `b≤0,1a`. En el primer registro `b/a≈0,492`: **no** cumple esa hipótesis. La diferencia entre aplicar la expresión completa y la simplificada al mismo `R` es **30,88 %** respecto a la simplificada; muestra la relevancia de no omitir la profundidad. Las cifras de la columna H.1 se reprodujeron mediante `2πaR`, pero esto **no demuestra** la inversión estratificada ni significa que 274,154 Ω·m sea la resistividad real del terreno de dos capas. **Pendiente:** inversión de `ρ_1/ρ_2/h` con fuente independiente y modelación de errores de medición.

## F. Benchmark independiente de malla — IEEE80 anexo H.3.1

**Fuente:** IEEE80 figura H.3 y tabla H.5, p. 200 (PDF p. 216). Malla de **70×70 m**, 5 espacios de 14 m por lado, `L_c=840 m`, sin varillas; `h=0,5 m`, `ρ=140 Ω·m`, `I_G=744,8 A`.

- Ecuación (57), sin varillas: **`R_g=1,047250 Ω`**, frente a **1,05 Ω** de la tabla H.5.
- `GPR=R_g I_G=779,9921 V`, frente a **780,0 V** publicados.
- En un intento independiente con `d=0,0105 m`, `n=6`, §16.5, la recomputación dio **`E_m=221,1693 V`** y **`E_s=91,6827 V`**; la tabla H.5 consigna **232 V y 96 V**, respectivamente. Diferencias de **4,67 %** y **4,50 %**. **Reconciliadas aritméticamente**: con 780 A las mismas ecuaciones dan 231,622 V y 96,016 V, que redondean a la tabla H.5. La figura y la introducción H.3 exigen 744,8 A. H.6 muestra la misma corriente implícita 780 A en otra geometría; ver diagnóstico.
- La tabla H.5 muestra asimismo un benchmark de otro programa (CDEGS): resistencia **1,00 Ω**, tensión en punto T1 **194,9 V** y paso S1 **89,3 V**, frente a **1,05 Ω, 232 V y 96 V** en columna IEEE. La comparación caracteriza **diferencias entre métodos** en puntos seleccionados, no un error exacto ni una tolerancia admisible.

**Estado F ACTUALIZADO:** `R_g/GPR` coherentes con 744,8 A, mientras que las columnas de tensiones H.5/H.6 reproducen 780 A; **inconsistencia de datos de referencia explicada**. Los resultados de programas comerciales siguen sin reproducirse.

## G. Evaluación del avance y límites

| Identificador | Comprobación | Resultado | Estado |
|---|---|---|---|
| V-01 | Térmica cobre B.1 | 34,0167 vs 34,02 kcmil | Coherente |
| V-02 | Térmica cobre-acero B.1 | 65,905 vs 59,81 kcmil | **Resuelto aritméticamente:** 6,814 vs 6,184 kA |
| V-03 | `K_f` 30 % a 1084 °C | 12,0669 vs 12,06 | Coherente |
| V-04 | `D_f`, cinco celdas tabla 10 | diferencias absolutas inferiores a 0,0003 | Coherente en 60 Hz |
| V-05 | `S_f` ejemplo §15.9 | 0,3671 vs 0,37 redondeado | Coherente |
| V-06 | Schwarz / matriz y escalamiento | 8,5201 Ω = inversión matricial | Comprobación algebraica; sin patrón independiente |
| V-07 | IEEE81 Wenner/H.1 | H.1 reproducida con `2πaR`; prueba de profundidad | Coherente y advertencia de dominio |
| V-08 | H.3 Grid 1 resistencia y GPR | 1,04725 Ω / 779,992 V vs 1,05 Ω / 780 V | Coherente |
| V-09 | H.3 Grid 1 tensión malla/paso | 221,17/91,68 V vs 232/96 V | **Resuelto aritméticamente:** 744,8 vs 780 A; confirmado también en Grid 2 |

**Próximos estudios sin cierre automático:** conservar V-02/V-09 como advertencias de referencia editorial, sin volver a tratarlos como fallas de fórmula; curvas y parámetros completos de Schwarz; `S_f` para sistemas con fuentes locales/remotas y anexo H.4; modelos de dos/múltiples capas y su interpretación independiente; ensayos de sensibilidad/casos límites y condiciones especiales (cercos/GIS/tensiones transferidas); contraste con exigencias SEC y sus textos complementarios; pruebas reales de campo solo mediante personal competente. El cumplimiento no se define por coincidencia de un par de fórmulas.

**Gobierno del proyecto:** etapa 0 **ABIERTA**; etapa 1 **EN CURSO**; **sin motor implementado**. Las pruebas anteriores son un instrumento de estudio, no una función de producto. El optimizador físico de dimensiones/reticulado sigue reservado a la etapa 10.

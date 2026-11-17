# c-oSPT — Resolución matemática de las discrepancias B.1 y H.3 de IEEE Std 80

**Fecha:** 2026-11-17. **Fuente primaria:** ejemplar adjunto de *IEEE Std 80-2013*, publicado 2015-05-15, que incorpora *IEEE Std 80-2013/Cor 1-2015*. **Estado:** inconsistencias aritméticas **explicadas y reproducidas** mediante sustituciones y contrapruebas; **NO** hay confirmación de errata oficial por IEEE ni validación integral del motor c-oSPT. **No copiar el PDF normativo al repositorio público.**

## Método de comprobación

1. Inspección visual directa de las páginas originales, para descartar pérdida de radicales, subíndices y exponentes en la extracción textual.
2. Comparación de los datos declarados con las ecuaciones de las cláusulas 11.3.1 y 16.5 y los anexos B.1 / H.3.
3. Cálculo con los datos impresos, inversión algebraica para deducir **qué entrada explica** el resultado publicado y contraste con un segundo caso diferente.
4. Separación entre la causa **numérica demostrada** y la causa **editorial histórica**, aún no documentada por una fe de erratas de IEEE.
5. Pruebas reproducibles sin dependencia de software externo ni datos reales.

## 1. Hallazgo B.1: sección térmica del conductor compuesto

### Referencias y datos

- IEEE80 §11.3.1, ecuación (46), anexo B.1, paso 2, ec. (B.3), **página impresa 131 / página PDF 147**; corriente de falla de la **página impresa 130 / PDF 146**.
- Corriente indicada y utilizada para el conductor: **6.814 kA**. Condiciones del material 30 % cobre-acero: tiempo 0.5 s, TCAP 3.85 J/(cm³·°C), α_r = 0.00378 °C⁻¹, ρ_r = 5.862 µΩ·cm, K₀ = 245 °C, Tm = 700 °C, Ta = 40 °C.
- Ecuación (46) con I expresada en kA y resultado en kcmil. Todos los demás valores se mantienen exactamente como están impresos; **no se sustituyó otra fórmula**.

### Sustitución e inversión

La combinación de constantes de B.1 da, para este material y tiempo,

`A_kcmil = 9.671996049231291 × I_kA`.

| Corriente introducida | Resultado de (46) |
|---|---:|
| **6.814 kA**, corriente declarada en B.1 | **65.904981 kcmil** |
| **6.184 kA**, inversión del orden de las cifras 1 y 8 | **59.811624 kcmil** |
| Resultado **publicado** en (B.3) | **59.81 kcmil** |

La inversión algebraica independiente de la fórmula da `I = 59.81/9.671996049231291 = 6.183832 kA`, redondeando **6.184 kA**. No es un problema de separador decimal ni de metodología térmica: el número publicado **corresponde exactamente a otra corriente** obtenida por transposición.

Como control auxiliar histórico, una reproducción en línea de *IEEE Std 80-2000* exhibe `6.184` en el mismo desarrollo junto al resultado `65.9` (incoherencia interna de esa transcripción). **No se presenta como errata oficialmente certificada**; el argumento principal se sostiene con el PDF recibido y la inversión aritmética.

### Valor de trabajo y seguridad

Con la corriente efectivamente declarada, usar **65.905 kcmil ≈ 33.3945 mm²**, equivalente a diámetro sólido `sqrt(4A/π) ≈ 6.5207 mm`, para reproducir este ejemplo térmico. El resultado editorial **59.81 kcmil / 30.24 mm² y diámetro 6.2 mm no es un patrón válido** con sus entradas publicadas. La conclusión ilustrativa de que un diámetro nominal de 10 mm supera el mínimo térmico calculado permanece verdadera para el ejemplo, pero **no** exime verificar materiales, construcción, corrosión, límites del método y pliegos chilenos.

**Clasificación B.1:** **DISCREPANCIA MATEMÁTICA RESUELTA** — valor impreso compatible con transposición `6.814 → 6.184`; **origen editorial exacto NO confirmado por IEEE**.

## 2. Hallazgo H.3: tensiones de malla y paso para grids 1 y 2

### Referencias y datos

- IEEE80 §16.5, ecuaciones (85)–(99), especialmente `K_m` (86), `K_i` (94), `L_M` (95)/(96), `L_S` (98) y `K_s` (99); **páginas impresas 94–96 / PDF 110–112**.
- Anexo H.3, introducción **página impresa 199 / PDF 215**: corriente **744.8 A para todos los casos**.
- Figuras H.3 y H.4 y tablas H.5 y H.6, **páginas impresas 200–201 / PDF 216–217**, repiten `I_G=744.8 A`.
- Malla cuadrada 70 × 70 m; 6 conductores por eje; separación 14 m; `L_C=840 m`, `n=6`, profundidad 0.5 m, conductor 2/0 Cu de diámetro `d≈0.0105 m`, resistividad uniforme `ρ=140 Ω·m`.
- Grid 1: sin varillas; Grid 2: veinte varillas de 7.5 m en perímetro, `L_R=150 m`; aplicar `K_{ii}=1` y `L_M` de (96), `L_S` de (98). No tratar ambos casos con `L_M` idéntica.

### Comparación de dos hipótesis, sin alterar geometría ni ecuaciones

| Caso y magnitud | Fórmulas IEEE con **744.8 A** (declarados) | Mismas fórmulas con **780 A** | Tabla editorial |
|---|---:|---:|---:|
| Grid 1, tensión de malla `E_m` | 221.169259 V | **231.621942 V** | **232 V**, H.5 |
| Grid 1, tensión de paso `E_s` | 91.682731 V | **96.015749 V** | **96.0 V**, H.5 |
| Grid 2, tensión de malla `E_m` | 155.265893 V | **162.603916 V** | **163 V**, H.6 |
| Grid 2, tensión de paso `E_s` | 76.250984 V | **79.854683 V** | **80 V**, H.6 |

**La misma corriente alternativa de 780 A reproduce las cuatro tensiones publicadas tras el redondeo editorial.** Esto descarta redondeo de `d` como causa general, ya que `E_s` no utiliza `d`; también descarta que sea una fórmula mejorada distinta, porque las ecuaciones publicadas bastan al cambiar solo la corriente.

**Control cruzado de redondeos:** al invertir cada tensión publicada, las corrientes inferidas son ~781.27 A (Grid 1 malla), ~779.87 A (Grid 1 paso), ~781.90 A (Grid 2 malla), ~781.42 A (Grid 2 paso). Todas son compatibles con **780 A** dentro del redondeo de una cifra decimal para el paso de H.5 y unidades enteras para las demás. La intersección de los cuatro intervalos de redondeo contiene `780 A` (aprox. **779.59–780.28 A**).

### Por qué no cambiar el dato H.3 de 744.8 A a 780 A

En H.5 la elevación de potencial publicada `GPR=780 V` **sí** resulta de `R_g≈1.04725 Ω × 744.8 A≈779.99 V`. En H.6 la resistencia publicada `R_g≈1.022 Ω` produce `GPR≈761.2 V` con 744.8 A, coherente con `761.0 V` de la tabla. Por tanto, **780 A aparece solamente como entrada compatible con las columnas de tensiones**, no con una modificación global y justificada de la corriente del estudio.

El valor `780` coincide numéricamente con el GPR de Grid 1, pero **no** con el GPR de Grid 2. No existe evidencia suficiente para afirmar que el editor convirtió erróneamente GPR en corriente; la explicación comprobable es **uso implícito de 780 A para las tensiones de ambas filas, pese a declarar 744.8 A**.

### Valores matemáticamente coherentes con los datos impresos

Para un ensayo reproducible basado en *las ecuaciones simplificadas* y **744.8 A**, los objetivos son:

- **Grid 1:** `R_g≈1.04725 Ω`, `GPR≈779.99 V`, `E_m≈221.17 V`, `E_s≈91.68 V`.
- **Grid 2:** con varillas y el método de §16.5, `E_m≈155.27 V` y `E_s≈76.25 V` (y `GPR≈761 V` desde la resistencia de la tabla H.6).

Son **valores derivados con entradas declaradas**, no reemplazos oficiales de las tablas de IEEE; los resultados comerciales CDEGS/ETAP/WinIGS están basados en otros métodos y tampoco deben tratarse como salidas idénticas de ecuaciones simplificadas.

**Clasificación H.3:** **DISCREPANCIA MATEMÁTICA RESUELTA** — columnas de tensiones de H.5/H.6 reproducibles con `780 A` en vez de los `744.8 A` indicados; **origen editorial exacto NO confirmado por IEEE**.

## 3. Reglas de implementación y evaluación futura

1. Los **datos de figura/introd.** `I_G=744.8 A` y los **resultados reconstruidos** deben almacenarse separadamente de los resultados editoriales de H.5/H.6; nunca sobrescribir referencias originales como si fueran una corrección oficial.
2. Las pruebas unitarias deben verificar ambas hipótesis, y clasificar las cifras impresas como **referencias de consistencia editorial, NO casos patrón de aceptación a 744.8 A**.
3. Bloquear fórmulas con datos faltantes o incompatibles, y no ajustar coeficientes, unidades ni constantes empíricas para forzar coincidencias.
4. Se han resuelto **estos dos problemas de consistencia matemática**, pero no se declara validado IEEE80 completo ni el motor de cálculo. Restan modelos de suelo, métodos de corriente, casos de campo, límites normativos y otras validaciones independientes.
5. No declarar «error oficial de IEEE» ni errata ratificada. Registrar **posible error editorial sustentado por análisis inverso**, pendiente de confirmación institucional.

## 4. Evidencia reproducible

Script autónomo: [diagnostico_inconsistencias_ieee80.py](./diagnostico_inconsistencias_ieee80.py). Comprueba ecuaciones, cuatro resultados de dos mallas, inversión algebraica térmica, control de redondeos, consistencia de GPR y prueba con las dos corrientes. Ejecutable en Python 3 estándar, sin archivos de usuario ni fuentes normativas reproducidas.

**Resultado del análisis:** **B.1 y H.3 RESUELTOS EN EL PLANO MATEMÁTICO; confirmación de causa histórica editorial pendiente, no inferida como hecho.**

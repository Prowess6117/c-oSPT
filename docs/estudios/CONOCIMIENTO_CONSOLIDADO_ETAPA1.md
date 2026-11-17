# c-oSPT — Conocimiento consolidado para continuidad de la etapa 1

**Actualización:** las diferencias B.1/H.3 están **RESUELTAS MATEMÁTICAMENTE**; véase [diagnóstico con inversiones y dos mallas](./DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md). No es una fe de erratas oficial.

**Fecha de corte:** 2026-11-17. **Estado:** registro de interpretación normativa inicial y conocimientos verificados **parcialmente**. No es una norma, no valida el motor de cálculo ni acredita conformidad de una instalación.

**Propósito:** evitar que hallazgos, hipótesis, restricciones, decisiones y pendientes técnicos se pierdan entre sesiones. Es complemento de [ESTUDIO_NORMATIVO_IEEE80_IEEE81_RIC06_RPTD06.md](./ESTUDIO_NORMATIVO_IEEE80_IEEE81_RIC06_RPTD06.md), no lo reemplaza. El estado del proyecto se rige por [ROADMAP](../../ROADMAP.md) y [AVANCE](../../AVANCE.md).

## 1. Evidencia normativa disponible y límites de uso

| Clave | Fuente revisada | Identidad de la copia aportada | Función |
|---|---|---|---|
| IEEE80 | *IEEE Guide for Safety in AC Substation Grounding* | **IEEE Std 80-2013**, copia de 226 páginas publicada 2015-05-15 e incorporando **IEEE Std 80-2013/Cor 1-2015** | Seguridad y diseño de mallas de subestaciones de CA |
| IEEE81 | *IEEE Guide for Measuring Earth Resistivity, Ground Impedance, and Earth Surface Potentials of a Grounding System* | **IEEE Std 81-2012**, copia de 86 páginas | Medición y evaluación de resistividad, impedancia, potenciales y ensayos |
| RIC06 | SEC, *Puesta a tierra y enlace equipotencial* | RIC N°06, resolución exenta 33.877 (2020-12-30); PDF adjunto de 27 páginas | Instalaciones de consumo BT/MT y remisiones |
| RPTD06 | SEC, *Puesta a tierra* | RPTD N°06, resolución exenta 33.277 (2020-09-10), modificada por 34.770 (2021-07-22); PDF adjunto de 9 páginas | Producción, transporte, almacenamiento y distribución |

Las ediciones son **las recibidas**: la actualización jurídica, nuevas erratas y vigencia de las disposiciones deben comprobarse antes del uso profesional. **Prohibido publicar el contenido íntegro de los PDF, sus páginas, datos de clientes, coordenadas o credenciales en este repositorio público.**

## 2. Campo de aplicación que sí se desprende de la lectura

- IEEE80 §§1.1–1.2: seguridad de puesta a tierra de subestaciones **de corriente alterna**, convencionales o GIS, principalmente exteriores; uso en interiores con cautela; orientada a 50/60 Hz. Quedan fuera el tratamiento específico de subestaciones de CC y el análisis cuantitativo de sobretensiones de rayo.
- IEEE81 §§1, 5–9: procedimientos y limitaciones de **medición**, no sustituto automático del diseño. Un estudio sintético no verifica una instalación real.
- RIC06 §§2 y 5.7: alcance de consumo BT/MT; para sistemas de tierra de alimentación AT/MT remite al RPTD06. Sus requisitos no se extrapolan indiscriminadamente.
- RPTD06 §§2, 5, 8.24–8.27: ámbito del sistema eléctrico, límites tolerables de paso/contacto y remisión explícita de cálculos a IEEE80-2013 (§8.25). El límite de resistencia en §8.27 **no sustituye** la revisión de tensiones peligrosas.
- **Alcance propuesto para v1, sin aprobación definitiva:** mallas de subestaciones de CA, con casos de suelo y geometría compatibles con cada procedimiento; clasificar previamente si corresponde RPTD, RIC o situación mixta.

## 3. Dependencias, variables y comprobaciones que se deben preservar

| Orden | Tema | Variables / datos relevantes | Fuente / precaución |
|---|---|---|---|
| 1 | Instalación y norma aplicable | régimen de instalación, acceso público, periferias, tiempo de protección | IEEE80 §§1, 8–10, 17; RIC06 §§2/5.7; RPTD06 §§2/5/8 |
| 2 | Modelo de suelo | resistividad aparente `ρ_a`, capas `ρ1/ρ2`, espesor, incertidumbre, orientación de sondas | IEEE81 §7; IEEE80 §§12–13; no confundir modelo interpretado con medición |
| 3 | Criterios fisiológicos | `t_s` (s), masa 50/70 kg justificada, `ρ_s` (Ω·m), `h_s` (m), `C_s` | IEEE80 §§5–8; RPTD06 §5; la elección de 70 kg no es automática |
| 4 | Solicitación térmica | corriente de conductor, `t_c` (s), `TCAP`, `α_r`, `ρ_r`, `T_a`, `T_m` y material | IEEE80 §11; límites mecánicos, térmicos y locales son controles adicionales |
| 5 | Malla y resistencia | `A`, `L_C`, `L_R`, `h`, separación `D`, diámetro `d`, cantidad/posición de varillas, `R_g` | IEEE80 §§9, 14, 16; modelos simplificados no universales |
| 6 | Falla y corriente | `3I_0`, `S_f`, `I_g`, `X/R`, `t_f`, `D_f`, `I_G`, `GPR` | IEEE80 §§15–16; no igualar corriente de conductor con inyección a tierra remota |
| 7 | Verificación de gradientes | `E_m`, `E_s`, `E_touch`, `E_step`, margen, modo de contacto | IEEE80 §§8, 16–17; evitar afirmar conformidad si falta transferencia/GIS/cercos |
| 8 | Contrastación y campo | ejemplos independientes, precisión, ensayos, resistividad real y documentación | IEEE80 anexos B/H y §19; IEEE81 §§5, 8–10; RPTD06 §§8.21–8.23 |

**Distinciones imprescindibles:** `t_f` no es necesariamente `t_s` ni `t_c`; `I_g` no es `I_G` ni la corriente total de falla; `R_g` y `GPR` no son tensiones de contacto; `ρ_s`, `ρ` y `ρ_a` no son intercambiables. En IEEE80 §16.4 los pasos de evaluación dependen del modelo y de las corrientes/capacidades de falla; seguir esa secuencia sin omitir bloqueos.

## 4. Restricciones y límites importantes

- IEEE80 §16.5–16.8: las ecuaciones aproximadas para `E_m/E_s` tienen **hipótesis de suelo uniforme, separación regular y supuestos geométricos**; casos complejos y suelos estratificados precisan procedimientos apropiados. El intervalo de configuraciones contrastado en §16.7 no es una licencia universal de extrapolación.
- Schwarz, IEEE80 §14.3: requiere `R1`, `R2`, `R_m` y coeficientes `k1/k2` con geometría/profundidad compatibles; revisar **gráfica** de Fig. 24, no solo texto extraído.
- IEEE81: los resultados de Wenner y la inversión de resistividad dependen de espaciamiento/profundidad, interferencias y modelo de suelo. Las mediciones de SPT pueden ser peligrosas; no automatizar decisiones de campo.
- IEEE80 §17: elementos metálicos, cercos, manijas y tensiones transferidas exigen revisión propia.
- RIC06, RPTD06: los requisitos normativos del ámbito chileno son obligatorios cuando sean aplicables, aunque las aproximaciones IEEE reproduzcan sus ejemplos.

## 5. Evidencias disponibles y estado

- **Reproducción exploratoria anterior:** diez contrastes numéricos de `R_g/E_m/E_s` de IEEE80 B.1–B.4 (diferencias relativas 0,038 %–1,200 % frente a tablas editoriales), Wenner algebraico y `C_s` con redondeos. No es validación independiente del motor.
- **Verificación térmica de cobre:** IEEE80 B.1 para 6,814 kA, `K_f=7,06`, `t_c=0,5 s` produce ≈34,02 kcmil, coherente con la guía.
- **Hallazgo B.1 resuelto matemáticamente:** el valor 59,81 kcmil es la sustitución con **6,184 kA**, frente a **6,814 kA** declarados. La salida correcta de (46) con los datos impresos es **65,905 kcmil ≈ 33,395 mm²**, diámetro sólido ≈6,521 mm. Posible transposición editorial; no ratificada por IEEE.
- **Hallazgo H.3 resuelto matemáticamente:** H.5 y H.6 imprimen tensiones compatibles con **780 A**, mientras introducción y figuras H.3/H.4 establecen **744,8 A**. Para esta última corriente, Grid 1 da 221,17/91,68 V y Grid 2 155,27/76,25 V en las ecuaciones simplificadas; los valores editoriales quedan registrados pero no se usan como patrones a 744,8 A.
- **Pendientes técnicos abiertos:** aplicación de `D_f`/`S_f` en dominios completos, Schwarz con modelos y límites de aplicación, suelo de dos/múltiples capas, benchmarking avanzado, materiales/temperaturas, casos especiales y medición/ensayos de campo.
- **Pendientes de seguridad/alcance etapa 0:** selección formal del primer tipo de instalación; `.gitignore`, licencia, procedimiento de contribución/revisión de secretos, política operativa de datos reales y decisiones tecnológicas.

## 6. Método de trabajo y reglas de cierre

Para cada nueva prueba: (i) abrir **página visual** y comprobar símbolos/radicales/subíndices; (ii) referenciar edición, sección y ecuación/tabla; (iii) declarar datos, unidades, hipótesis y dominio; (iv) calcular con precisión completa, comparar referencia editorial o control independiente; (v) informar diferencia absoluta y relativa y sus posibles causas **solo si están demostradas**; (vi) clasificar `comprobado algebraicamente`, `coherente con ejemplo`, `discrepante`, `no evaluable` o `fuera de alcance`; (vii) registrar código de prueba si se decide publicarlo, nunca PDFs ni expedientes reales.

La etapa 0 sigue **ABIERTA** y la etapa 1 **EN CURSO**. Ninguna prueba de estas páginas confiere sello IEEE/SEC, prueba de seguridad real o autorización para programar un motor sin cerrar el análisis crítico. La optimización geométrica permanece en **etapa 10**, última.

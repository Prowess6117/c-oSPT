# c-oSPT — Alcance de la primera implementación

**Fecha de decisión técnica:** 2026-11-17. **Estado:** alcance inicial limitado para desarrollo, NO aprobación de uso en obra real.

## Primera versión candidata (v0.1, todavía inexistente)
- **Instalaciones:** diseño preliminar y verificación parcial de mallas para **subestaciones exteriores de corriente alterna (50/60 Hz)**, conforme al campo de la guía IEEE Std 80.
- **Geometría:** cuadrada o rectangular, conductores horizontales en reticulado **regular y espaciado uniformemente**; electrodos verticales solo si el método seleccionado los representa.
- **Suelo:** uniforme **únicamente si mediciones e interpretación lo justifican**. Un promedio aritmético no demuestra homogeneidad.
- **Condiciones:** corriente de falla y parte que entra a tierra, tiempo, materiales y temperaturas, superficie, dimensiones y construcción deben proceder de fuentes documentadas; sin defaults críticos.
- **Normativa base de estudio:** IEEE Std 80-2013 incorporando Cor 1-2015; IEEE Std 81-2012 para mediciones. Clasificar correctamente la instalación y aplicar pliegos chilenos RIC/RPTD según su ámbito y versión efectiva.
- **Resultados futuros:** resistencia, GPR, tensiones admisibles y calculadas, secciones y verificaciones modeladas, con trazabilidad y límites. Ningún resultado es válido hasta implementar y contrastar el motor.

## Restricciones
**No aplicar automáticamente** expresiones del suelo uniforme a terrenos estratificados; tampoco a suelos lateralmente heterogéneos, reticulados no uniformes, mallas irregulares, GIS, CC, rayos, cercos, tensiones transferidas, tuberías/rieles/cables externos o reparto complejo de falla no justificado.

Si para el caso real hacen falta verificaciones fuera del método, mostrar **NO EVALUABLE** o **FUERA DE ALCANCE**: no emitir aprobación global. Una baja resistencia por sí sola no implica seguridad.

## Crecimiento
Conservar en README el objetivo final amplio para mallas de puesta a tierra en Chile. Extender a instalaciones de consumo, suelos múltiples o geometrías especiales exige estudio y validación propios. **Optimizador geométrico reservado exclusivamente a la última etapa 10**.

## Evidencia
Esta limitación procede del estudio documental de etapa 1:
[ETAPA1_MATRIZ_Y_CRITERIOS_DE_CIERRE.md](./estudios/ETAPA1_MATRIZ_Y_CRITERIOS_DE_CIERRE.md), sección 2. La decisión limita lo que se programará primero, **no interpreta automáticamente un caso concreto**.

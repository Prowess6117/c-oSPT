# c-oSPT — Política y diseño pendiente de licencias por clave

**Fecha:** 2026-11-17. **Estado:** decisión de producto registrada; sin implementación, claves emitidas ni activación operativa.

## Decisiones confirmadas

1. El repositorio permanece **público**, pero el código y documentación originales son de **derechos reservados** y se distribuyen bajo [licencia restrictiva beta](../LICENSE.md); no es código abierto con uso comercial libre.
2. **Modalidad personal/educativa:** no comercial, autorizada por el titular; cuando exista activación, requerirá clave propia emitida por el titular.
3. **Modalidad comercial:** prohibida por defecto durante beta; solo admisible si el titular entrega **permiso expreso por escrito** y la correspondiente clave comercial al implementarse el sistema.
4. Ambas modalidades tienen límites de alcance; la existencia de licencia **no convierte el motor en software validado**, ni exime de verificación por profesional competente.
5. El usuario deberá solicitar la licencia al titular; se definirá un **canal privado** sin publicar dirección personal, ubicación o claves de administración.

## Diseño de seguridad recomendado (a investigar, no implementado)

- Para conservar la arquitectura PWA local-first sin backend, evaluar **licencias firmadas digitalmente** de forma asimétrica. Un emisor fuera del repositorio firma una licencia con clave privada; la aplicación contiene solo la **clave pública de verificación**, que no es secreto.
- La licencia debería incluir, como mínimo y sin datos personales innecesarios: identificador aleatorio de licencia, modalidad personal/educativa o comercial, versión de esquema, vigencia si se autoriza, y firma criptográfica. No incorporar nombre, correo ni identificador de dispositivo sin justificación y autorización.
- **Nunca** alojar la clave privada de emisión en GitHub, JavaScript, archivos distribuidos, GitHub Actions ni scripts públicos. Diseñar custodia y copias de recuperación fuera del repositorio.
- Validar firma, modalidad, fechas y estado de licencia según requerimientos formalmente definidos. No usar una clave secreta compartida en el navegador ni considerar ofuscación como protección suficiente.
- El uso completamente offline tiene límites de **revocación y control de reloj**. La validación en el navegador es alterable por quien controla el equipo y el código fuente; las claves dificultan distribución accidental, **no impiden de forma robusta eliminar el control de licencias**.
- No introducir servidor de activación, rastreadores, telemetría, cuentas o recolección de IP sin un nuevo análisis de amenazas, costos y consentimiento del propietario.
- Separar permiso **jurídico** de mecanismo **técnico**: una licencia comercial requiere tanto autorización escrita como clave; superar un control técnico nunca concede derechos legales.

## Etapas de trabajo

**Etapa 0:** establecer condiciones y registrar decisiones — este archivo y LICENSE.md. **Sin claves ni código.**

**Etapa 2:** incluir en el modelo de datos y arquitectura una interfaz opcional de autorización/licencia separada del motor matemático; definir escenarios de prueba y criterios de privacidad, sin bloquear pruebas de validación internas.

**Etapas 7–9:** antes de cualquier distribución utilizable, diseñar e implementar el sistema de emisión/verificación si se mantiene la decisión, probar casos válidos, inválidos, expirados, manipulados, modalidades y funcionamiento sin red. Auditar dependencia criptográfica y almacenamiento; registrar restricciones conocidas. No inventar protección absoluta ni migrar a backend sin autorización.

**Etapa 10:** el optimizador sigue siendo la última etapa técnica de cálculo. **El licenciamiento no altera el orden de validación eléctrica**.

## Pendientes del titular

- Elegir el canal privado de solicitud y el documento/medio de permiso escrito comercial.
- Decidir si ambas modalidades tienen expiración, límite de equipos o renovación; no adoptar restricciones silenciosas.
- Evaluar con asesoría jurídica el texto final de licencia y las autorizaciones comerciales.
- Determinar cuándo habrá una versión utilizable: hoy solo hay documentación y scripts de investigación.

**Criterio de aceptación futuro:** un flujo documentado de emisión y validación que no publique secretos, diferencie modalidades, preserve la privacidad y describa con precisión el límite de protección de un cliente web público.
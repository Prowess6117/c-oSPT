# c-oSPT — Política de privacidad y datos

**Fecha:** 2026-11-17. Política de diseño de etapa 0: no significa que exista una implementación de almacenamiento.

## Clasificación
| Clase | Ejemplos | Tratamiento |
|---|---|---|
| Pública autorizada | Código propio, análisis y casos 100 % sintéticos | GitHub tras revisión |
| Normativa protegida | PDF IEEE y terceros con copyright | Lectura privada; nunca repositorio |
| Técnica privada | Mediciones reales, IP2Win, resistividad, planos, informes, nombres, coordenadas | No subir ni a GitHub, issues o PR |
| Secretos | Tokens, API keys, contraseñas, certificados y archivos de entorno | Nunca versionar ni incrustar en cliente |
| Identificadores | IP, correo, rutas del equipo y metadatos | Minimizar; no publicar inadvertidamente |

## Flujo previsto
1. Procesar los datos de ingeniería localmente en el dispositivo; sin backend, cuentas, analítica, geolocalización ni peticiones externas por defecto.
2. Mantener el caso inicialmente en memoria de sesión. No asumir que el almacenamiento del navegador es cifrado ni persistente.
3. Importación y exportación **manual**, con validación de contenido, tamaño y metadatos; el usuario decide dónde se guarda el archivo.
4. Generación local de informes. Inspeccionar identificadores y propiedades del PDF antes de una eventual divulgación.
5. GitHub sincroniza **código y documentación no sensible**, nunca casos reales. Para mover casos entre computadores, exportación privada consciente del usuario.
6. Si se implementa PWA offline, cachear solo recursos aprobados de la aplicación, nunca expedientes por defecto.

## Riesgos y respuestas
- El alojamiento del sitio puede registrar la IP del visitante; la ausencia de backend propio no ofrece anonimato.
- En computadores compartidos, extensiones maliciosas o malware podrían leer datos locales. El guardado cifrado, si se implementa, requiere análisis y advertencias reales.
- .gitignore no impide git add -f, filtraciones dentro de archivos permitidos ni elimina historial.
- En caso de exposición de token: **revocar/rotar**, identificar compromisos y verificar historial. Un cambio de configuración no elimina automáticamente commits previos.

## Antes de publicar
Revisar archivos preparados, metadatos, comentarios, capturas y ejemplos; excluir cualquier dato no autorizado. No enviar estos datos a servicios de terceros ni copiarlos a logs, URL o pruebas. Sin datos críticos suficientes, bloquear cálculos o etiquetar NO EVALUABLE.

## Pendientes posteriores (no implementarlos en etapa 0)
Formatos de importación/exportación, retención/borrado local, cifrado opcional, validación de archivos, seguridad de service worker y comprobación de solicitudes de red. Se desarrollarán cuando su etapa corresponda.

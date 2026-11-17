# Seguridad de c-oSPT

Repositorio público de **desarrollo experimental**; no existe aún un motor validado ni producto apto para tomar decisiones de seguridad eléctrica.

## Política
- Publicar solo código y documentación propios, ejemplos sintéticos y material con permisos explícitos.
- Nunca publicar información técnica real de clientes, ubicaciones, direcciones IP, geodatos, planos, estudios, certificados privados, contraseñas, tokens ni PDF normativos protegidos.
- El diseño elegido es local-first y sin backend, cuentas, telemetría ni geolocalización por defecto. No prometer anonimato: el proveedor del sitio puede registrar IP y el equipo o navegador puede almacenar información local sin cifrar.
- Ningún módulo no validado podrá presentar resultados como ingeniería aprobada.

## Informe de vulnerabilidades
No registrar secretos, datos reales ni exploits sensibles en un issue público. Si está habilitado GitHub Private Vulnerability Reporting, usarlo. Si no lo está, solicitar primero al propietario un canal privado; no se publica aquí una dirección personal.

Si se filtra una credencial: revocarla o rotarla en origen, suspender uso/publicación afectada, investigar archivos e historial y evaluar saneamiento. Borrar un archivo de la última versión no elimina copias anteriores.

## Verificación previa a cada publicación
- Revisar estado, archivos y diferencias preparados para commit, incluso metadatos y comentarios.
- Comprobar que no se integren dependencias, solicitudes de red o permisos nuevos sin revisión.
- Para código numérico: evidencia de fuente, unidades, dominio, límites, pruebas y regresión.
- Para importaciones: validar tipo, tamaño, estructura y tratamiento seguro del contenido.
- Los escáneres y .gitignore son auxiliares; no dan garantía absoluta.

## Controles administrativos pendientes — excepciones de etapa 0

El propietario decidió **posponer** estas configuraciones y cerrar **documentalmente** la etapa 0, sin dar por mitigados los riesgos. Se documentan en [BACKUP_DOCUMENTAL.md](./BACKUP_DOCUMENTAL.md). **No equivale a seguridad verificada.**

## Pendientes que requieren configuración real
- Protección de la rama main.
- Privacidad del correo de commits y bloqueo de pushes que divulguen correo privado.
- Licencia beta **definida**, restrictiva y de derechos reservados ([LICENSE.md](./LICENSE.md)); las claves personal/educativa y comercial están **planificadas, no implementadas**.
- Revisión del historial completo y activación de alertas de secretos si están disponibles.

Véanse CONTRIBUTING.md, docs/POLITICA_DATOS.md y docs/ETAPA0_AUDITORIA_SEGURIDAD.md.

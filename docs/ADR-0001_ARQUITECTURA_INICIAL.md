# ADR-0001 — Decisión inicial de arquitectura

**Fecha:** 2026-11-17. **Estado:** propuesta arquitectónica adoptada para planificación, revisable según pruebas; sin dependencias instaladas ni stack definitivo.

## Necesidad
Herramienta personal de ingeniería en Chile, código público en GitHub, acceso desde diferentes computadores, tratamiento privado de expedientes, motor reproducible y generación local de informes.

## Alternativas comparadas
| Opción | Ventajas | Costos y riesgos | Decisión |
|---|---|---|---|
| Escritorio nativo/empaquetado | Control de ficheros y funcionamiento local | Builds multiplataforma, mantenimiento de instaladores y actualizaciones | Posponer |
| Aplicación web con backend y framework completo | UI y sincronización amplias | Cuentas, servidor, redes, secretos y superficie de ataque innecesarios | No usar en v0.1 |
| **Web estática PWA local-first** | Acceso desde varios PC; sin backend; opción offline; fácil distribuir código | Navegador no cifra datos por sí mismo; cuidado de caché, importaciones y terceros | **Preferida** |

## Diseño acordado
- **Motor:** funciones puras aisladas del DOM, red y almacenamiento; unidades, verificaciones de dominio, referencias normativas y pruebas independientes.
- **Frontend:** interfaz mínima web basada en módulos; **TypeScript como candidato preferido** por la claridad del contrato de datos. Comparar implementación sin framework de UI frente a librerías según el tamaño real de formularios.
- **Herramientas de build/test:** contrastar Vite/Vitest con herramientas mínimas de TypeScript/Node y navegador. Elegir versiones y lockfile en etapa 2 tras revisar licencias, vulnerabilidades, mantenimiento y reproducibilidad. Ningún paquete está aprobado aún.
- **Persistencia:** inicialmente memoria en sesión; archivos de proyecto solo mediante importación/exportación consciente, tras validar seguridad.
- **Offline:** manifest y service worker solo tras pruebas de funcionamiento, caché y permisos.
- **Publicación:** GitHub Pages NO habilitado por esta decisión; se resolverá tras auditoría de etapa 9.
- **Informes:** generación local; biblioteca y formato pendientes de revisión y pruebas.

## Reconsiderar si
El navegador no permite una función exigida, falla una validación de precisión, las dependencias generan riesgos injustificados o la privacidad necesita otra arquitectura. Documentar nueva ADR antes de cambiar.

El **optimizador** buscado por el usuario modifica geometría y reticulado **físicos**, y se programa únicamente en etapa 10, después del motor verificado.

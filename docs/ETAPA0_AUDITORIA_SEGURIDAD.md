# Etapa 0 — Auditoría preliminar del repositorio

**Fecha:** 2026-11-17. **Ámbito comprobado:** árbol actual y metadatos recientes visibles de GitHub, más búsqueda de patrones en los doce archivos de texto anteriores a este cambio. No es auditoría integral del historial ni prueba de una app inexistente.

## Evidencia observada
- Repositorio público Prowess6117/c-oSPT, rama main; la consulta de ramas mostró **protected: false**.
- Antes de este cambio: README, ROADMAP, AVANCE y estudios/scripts en docs/estudios; **sin PDF ni planillas de clientes** entre los archivos del árbol vigente.
- En doce archivos de texto revisados no se detectaron patrones característicos de claves privadas o tokens habituales ni direcciones de correo dentro del contenido. **No equivale a certificar ausencia de secretos**.
- Algunos números con apariencia de coordenadas correspondían a **comparaciones numéricas de prueba** en scripts, verificado por contexto.
- Se observó una **dirección de correo personal en metadatos públicos de commits anteriores**; no se reproduce aquí.
- NO se escaneó exhaustivamente todo el historial ni forks/clones, no se revisaron dependencias futuras y no se ejecutaron pruebas de seguridad de una aplicación.

## Medidas incorporadas a la rama de trabajo
- .gitignore: filtro preventivo no retroactivo.
- SECURITY.md y CONTRIBUTING.md: protocolo de reporte y cambios.
- docs/POLITICA_DATOS.md: clasificación de información y flujos.
- docs/ETAPA0_ALCANCE_INICIAL.md: primer dominio de cálculo limitado.
- docs/ADR-0001_ARQUITECTURA_INICIAL.md: opciones y justificación.
- ROADMAP/AVANCE actualizarán solo las tareas con evidencia.

## Configuraciones reales pendientes del propietario
1. **Privacidad correo:** en GitHub Settings > Emails, habilitar Keep my email addresses private y Block command line pushes that expose my email. Configurar correo noreply en futuros commits; revisar el historial existente por separado.
2. **Protección main:** Repository Settings > Branches o Rules > Rulesets; bloquear force pushes y borrados; establecer Pull Request como vía normal. No activar checks obligatorios inexistentes.
3. **Licencia:** DECISIÓN POSTERIOR REGISTRADA: derechos reservados mediante [LICENSE.md](../LICENSE.md), personal/educativa autorizada y comercial con permiso escrito. Claves planificadas pero no implementadas. Se recomienda revisión jurídica del texto de licencia personalizada antes de distribución utilizable.
4. **Secret scanning:** consultar las funciones disponibles en Security/Settings, activar y verificar alertas/protección de push cuando sea posible.
5. **Auditoría histórica:** revisar commits anteriores, especialmente el correo de autor; reescribir historial requiere una evaluación de impactos y no garantiza borrar copias replicadas.

## Criterio de cierre pendiente
La etapa 0 no puede cerrarse solo porque los documentos existan: la licencia beta ya está definida, pero falta confirmar controles efectivos de GitHub y seguridad del historial. Tampoco se puede presentar la revisión por patrones como prueba definitiva.

Documentación oficial útil:
- https://docs.github.com/en/account-and-profile/how-tos/email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

## Verificación y aceptación posterior — 2026-11-17

Se revisaron **21 archivos rastreados** del árbol vigente, la integridad de sus enlaces Markdown y los **nombres de rutas modificadas en 32 commits** accesibles; no se detectaron PDF normativos o archivos privados obvios ni coincidencias de formatos habituales de secretos en el contenido actual. El alcance **no** fue escaneo forense de todo el contenido histórico. Se reconfirmó `main` sin protección y metadatos de autor que incluyen una dirección potencialmente personal, no reproducida aquí.

**El propietario pidió omitir las configuraciones de rama por ahora y cerrar documentalmente etapa 0.** La excepción se documentó como SEC-00-01/04 en [BACKUP_DOCUMENTAL](../BACKUP_DOCUMENTAL.md). No afirmar que esos controles fueron activados; el criterio original de ausencia demostrada de información personal en todo el historial no puede considerarse íntegramente satisfecho. La siguiente etapa puede planificarse, pero la distribución/uso profesional seguirá condicionada por evaluación de seguridad y validación del motor.

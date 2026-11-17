# Procedimiento de cambios — c-oSPT

Proyecto de uso personal con código público. No incorporar contribuciones externas o licencias ajenas sin revisión de titularidad. La licencia pública del código está pendiente de elección del propietario.

## Flujo acordado
1. Leer README.md, ROADMAP.md y AVANCE.md de main y comprobar etapa/alcance antes de modificar.
2. Crear una rama específica desde main; limitar los cambios a un objetivo.
3. Separar implementación matemática de interfaz y de persistencia.
4. Antes de publicar, ejecutar: git status --short; git diff --check; git diff --cached --stat; git diff --cached. Revisar también nombres, metadatos y datos privados.
5. Abrir Pull Request a main, con objetivo, referencias, riesgos, archivos y pruebas.
6. Revisar el PR antes de fusionarlo; no fusionar cambios sin evidencia requerida de seguridad o ingeniería.
7. Verificar el contenido resultante en main; registrar hito en ROADMAP y AVANCE si corresponde. Ante un error, revertir de modo trazable.

## Checklist de revisión
- [ ] Alcance y etapa respetados.
- [ ] Sin datos reales, coordenadas, credenciales ni PDF protegidos.
- [ ] Referencias normativas comprobables y licencia de dependencias revisada.
- [ ] Ecuaciones con variables, unidades, hipótesis, dominio y contrastes independientes cuando proceda.
- [ ] Pruebas ejecutadas y resultados registrados (o motivo de no aplicabilidad).
- [ ] Ningún resultado no validado se declara conforme.
- [ ] Se verificó el repositorio tras publicar.

Los scripts existentes en docs/estudios son **exploratorios**, no pruebas de un motor inexistente. No imponer checks automáticos que todavía no se han implementado.

**Limitación:** este documento no activa protección de main. La configuración debe efectuarse en los ajustes de GitHub.

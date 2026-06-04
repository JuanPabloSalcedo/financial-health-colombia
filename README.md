# Predicción de salud financiera empresarial en Colombia

Sistema de alerta temprana que, a partir de los ratios financieros de una
empresa en un año, predice su categoría de salud financiera en el año
siguiente. Basado en estados financieros de la Superintendencia de
Sociedades y en el Z''-Score de Altman para mercados emergentes.

## Estado
En construcción.

## Estructura
- `data/` datos crudos y procesados
- `notebooks/` análisis paso a paso (01 carga, 02 ratios, 03 EDA, 04 modelo)
- `src/` funciones reutilizables (ratios, Altman)
- `tests/` pruebas unitarias
- `outputs/` figuras y modelo entrenado
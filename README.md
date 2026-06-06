# Predicción de salud financiera empresarial en Colombia

Sistema de alerta temprana que, a partir de los ratios financieros de una empresa
en un año, predice su categoría de salud financiera en el año siguiente. Trabaja
con los estados financieros internos de empresas colombianas (perspectiva de
gestión interna) para anticipar el deterioro financiero antes de que ocurra.

## Motivación

A diferencia de un análisis de mercado (visión externa, basada en precios de
acciones), este proyecto adopta la mirada interna de la gestión: usa los estados
financieros reportados a la Superintendencia de Sociedades para conectar el perfil
de ratios de una empresa con decisiones concretas de gestión.

## Enfoque metodológico

- **Etiqueta objetiva con el Z''-Score de Altman.** En lugar de inventar una
  etiqueta de "salud", se usa el Z''-Score para mercados emergentes (Altman, 1995),
  apropiado para empresas privadas y no manufactureras, que son la mayoría del
  tejido empresarial colombiano.
- **Planteamiento temporal (alerta temprana).** Los ratios del año *t* predicen la
  categoría de salud en *t+1*. Esto evita la circularidad de predecir una etiqueta
  con las mismas variables que la generan, y hace del proyecto una herramienta
  predictiva real, no descriptiva.

## Datos

Estados financieros bajo NIIF (entradas "Plenas individuales") reportados a la
Superintendencia de Sociedades de Colombia, vía el portal SIIS, años 2018–2024.
Panel final: ~20.000 observaciones empresa-año.

Limitaciones conocidas: posible exclusión de empresas en proceso concursal;
las empresas preoperativas tienen ratios degenerados; las financieras y holdings
con frecuencia no reportan ingresos operacionales.

## Estructura

financial-health-colombia/
├── data/ (raw / processed)
├── notebooks/ (01_carga, 02_ratios, 03_eda, 04_modelo)
├── src/ (ratios.py, altman.py)
├── tests/
├── outputs/
├── README.md
└── requirements.txt

## Reproducir

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

Luego ejecutar los notebooks en orden (01 → 04).

## Estado actual

- [x] Carga, limpieza y unión de estados financieros (Fase 1)
- [x] Cálculo de ratios financieros (Fase 2, parcial)
- [ ] Z''-Score y etiqueta temporal
- [ ] Análisis exploratorio (Fase 3)
- [ ] Modelo de clasificación (Fase 4)
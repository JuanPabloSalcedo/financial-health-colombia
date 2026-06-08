import pandas as pd
from src.altman import clasificar_zona, calcular_zscore


def test_clasificar_zona():
    assert clasificar_zona(3.0) == "segura"
    assert clasificar_zona(1.5) == "gris"
    assert clasificar_zona(0.5) == "riesgo"
    assert clasificar_zona(float("nan")) is None


def test_zscore_valor_conocido():
    df = pd.DataFrame({
        "activo_corriente": [100], "activo_total": [200],
        "pasivo_corriente": [50], "pasivo_total": [100],
        "ganancias_acumuladas": [40], "utilidad_operacional": [30],
        "patrimonio": [100],
    })
    r = calcular_zscore(df)
    # X1=0.25, X2=0.2, X3=0.15, X4=1.0 Z'' = 4.35
    esperado = 6.56*0.25 + 3.26*0.2 + 6.72*0.15 + 1.05*1.0
    assert abs(r["zscore"].iloc[0] - esperado) < 1e-9
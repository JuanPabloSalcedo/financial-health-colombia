import pandas as pd
from src.ratios import calcular_ratios


def test_ratios_valores_conocidos():
    df = pd.DataFrame({
        "activo_corriente": [100], "activo_total": [200],
        "pasivo_corriente": [50], "pasivo_total": [120],
        "ganancias_acumuladas": [30], "patrimonio": [80],
        "ingresos": [400], "utilidad_operacional": [40], "utilidad_neta": [20],
    })
    r = calcular_ratios(df)
    assert r["razon_corriente"].iloc[0] == 2.0
    assert r["endeudamiento"].iloc[0] == 0.6
    assert r["roa"].iloc[0] == 0.1
    assert r["rotacion_activos"].iloc[0] == 2.0


def test_division_por_cero_es_nan():
    df = pd.DataFrame({
        "activo_corriente": [100], "activo_total": [200],
        "pasivo_corriente": [0], "pasivo_total": [120],
        "ganancias_acumuladas": [30], "patrimonio": [80],
        "ingresos": [400], "utilidad_operacional": [40], "utilidad_neta": [20],
    })
    r = calcular_ratios(df)
    assert pd.isna(r["razon_corriente"].iloc[0])
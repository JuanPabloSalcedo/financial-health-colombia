"""Cálculo del Z''-Score de Altman (modelo para mercados emergentes)
y clasificación de la salud financiera.

Referencia: Altman (1995), Z''-Score para mercados emergentes, apropiado
para empresas privadas y no manufactureras.
"""
import numpy as np
import pandas as pd

# Coeficientes del Z''-Score para mercados emergentes
C1, C2, C3, C4 = 6.56, 3.26, 6.72, 1.05

# Umbrales de las zonas de salud
UMBRAL_SEGURA = 2.6
UMBRAL_RIESGO = 1.1


def calcular_zscore(df):
    """Calcula los componentes X1–X4 y el Z''-Score.

    Recibe un DataFrame con las cuentas y devuelve una copia con las
    columnas x1, x2, x3, x4 y zscore añadidas.
    """
    df = df.copy()

    # X1: capital de trabajo / activos (liquidez)
    df["x1"] = (df["activo_corriente"] - df["pasivo_corriente"]) / df["activo_total"]
    # X2: utilidades retenidas / activos (rentabilidad acumulada)
    df["x2"] = df["ganancias_acumuladas"] / df["activo_total"]
    # X3: utilidad operacional / activos (rentabilidad operativa, EBIT)
    df["x3"] = df["utilidad_operacional"] / df["activo_total"]
    # X4: patrimonio / pasivos (solvencia)
    df["x4"] = df["patrimonio"] / df["pasivo_total"]

    df["zscore"] = C1 * df["x1"] + C2 * df["x2"] + C3 * df["x3"] + C4 * df["x4"]

    df = df.replace([np.inf, -np.inf], np.nan)

    return df


def clasificar_zona(zscore):
    """Clasifica un Z''-Score en 'segura', 'gris' o 'riesgo'."""
    if pd.isna(zscore):
        return None
    if zscore > UMBRAL_SEGURA:
        return "segura"
    elif zscore >= UMBRAL_RIESGO:
        return "gris"
    else:
        return "riesgo"
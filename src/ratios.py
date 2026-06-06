"""Funciones para calcular los ratios financieros del proyecto."""
import numpy as np


def calcular_ratios(df):
    """Calcula los ratios financieros a partir de las cuentas del panel.

    Recibe un DataFrame con las columnas de cuentas y devuelve una COPIA
    con las columnas de ratios añadidas.
    """
    df = df.copy()

    # Liquidez
    df["razon_corriente"] = df["activo_corriente"] / df["pasivo_corriente"]

    # Endeudamiento
    df["endeudamiento"]  = df["pasivo_total"] / df["activo_total"]
    df["apalancamiento"] = df["pasivo_total"] / df["patrimonio"]

    # Rentabilidad
    df["roa"]                = df["utilidad_neta"] / df["activo_total"]
    df["margen_neto"]        = df["utilidad_neta"] / df["ingresos"]
    df["margen_operacional"] = df["utilidad_operacional"] / df["ingresos"]

    # Eficiencia
    df["rotacion_activos"] = df["ingresos"] / df["activo_total"]

    # Las divisiones por cero generan infinitos, se pasan a Na
    df = df.replace([np.inf, -np.inf], np.nan)

    return df
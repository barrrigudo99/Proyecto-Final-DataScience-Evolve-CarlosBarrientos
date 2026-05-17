"""
cleaner.py
==========
Primera capa de limpieza del DataFrame crudo. Estandariza formatos,
imputa valores faltantes y elimina registros no válidos.

Funciones:
    limpiar_precios(df)         — Convierte strings de precio a float
    limpiar_metros(df)          — Extrae el número de strings como "85 m²"
    imputar_nulos(df)           — Imputa nulos con mediana (num) o moda (cat)
    eliminar_outliers(df)       — Elimina precios fuera del rango IQR × 3
    estandarizar_ciudades(df)   — Normaliza nombres de ciudades a minúsculas

Uso:
    from src.preprocessing.cleaner import limpiar_precios, eliminar_outliers
    df = limpiar_precios(df_raw)
    df = eliminar_outliers(df, columna="precio_mes")
"""

# TODO: importar pandas, numpy
# TODO: regex para extraer números de precios y metros
# TODO: IQR para detección de outliers con parámetro k configurable

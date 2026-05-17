"""
feature_extractor.py
====================
Ingeniería de features: crea variables derivadas que mejoran la predicción
y enriquecen el análisis exploratorio.

Features creadas:
    precio_m2          — precio_mes / metros
    es_zona_premium    — bool: distrito en lista de zonas premium por ciudad
    distancia_centro   — km al centro de la ciudad (haversine)
    ratio_hab_metros   — habitaciones / metros (densidad)
    anio_scraping      — año extraído de fecha_scraping
    mes_scraping       — mes extraído de fecha_scraping

Uso:
    from src.preprocessing.feature_extractor import agregar_features
    df = agregar_features(df_limpio)
"""

# TODO: importar pandas, numpy
# TODO: función haversine(lat1, lon1, lat2, lon2) → float km
# TODO: diccionario ZONAS_PREMIUM por ciudad desde config/config.yaml
# TODO: función agregar_features(df) que aplica todas las transformaciones

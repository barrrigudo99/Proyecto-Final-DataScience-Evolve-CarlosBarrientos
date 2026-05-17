"""
src.preprocessing
=================
Pipeline de preprocesado de datos. Transforma el DataFrame crudo extraído
por los scrapers en features listos para el modelo de ML.

Módulos:
    cleaner           — Limpieza: nulos, formatos incorrectos, outliers
    normalizer        — Escalado/codificación de variables para ML
    feature_extractor — Ingeniería de features: precio/m², zona premium, etc.
"""

"""
tools.py
========
Herramientas (tools) que el agente LangGraph puede invocar para responder
preguntas sobre el mercado de alquiler. Cada tool es una función decorada
con @tool de LangChain.

Tools disponibles:
    buscar_anuncios(query, ciudad, precio_max, metros_min)
        → Lista de anuncios que coinciden con los criterios

    estadisticas_mercado(ciudad, tipo)
        → Precio medio, mediana, percentiles, evolución para una ciudad

    predecir_precio(metros, habitaciones, ciudad, distrito)
        → Predicción de precio mensual usando el modelo de ML de 02_ml_models/

    comparar_ciudades(ciudades)
        → Tabla comparativa de precios entre varias ciudades

    top_barrios_por_precio(ciudad, n, orden)
        → Ranking de los n barrios más caros/baratos de una ciudad

Uso:
    from 03_rag_agent.src.tools import buscar_anuncios, predecir_precio
    # Las tools se pasan al agente en agent.py
"""

# TODO: from langchain.tools import tool
# TODO: from src.database.crud import obtener_inmuebles, obtener_estadisticas_ciudad
# TODO: from 02_ml_models.predict import predecir_precio as _predecir
# TODO: from 03_rag_agent.src.retriever import InmuebleRetriever

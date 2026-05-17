"""
Paquete 03_rag_agent
====================
Agente inteligente basado en RAG (Retrieval-Augmented Generation) y LangGraph
para responder preguntas en lenguaje natural sobre el mercado de alquiler español.

Notebooks (desarrollo iterativo):
    05_rag_setup        — Construcción del índice vectorial y pruebas de recuperación
    06_agente_langgraph — Implementación del grafo de agente con LangGraph

Módulo src/:
    document_loader — Convierte anuncios de la BD en documentos para ChromaDB
    embeddings      — Genera y persiste los embeddings con OpenAI
    vector_store    — Wrapper de ChromaDB para búsqueda semántica
    retriever       — Estrategia de recuperación (similarity + MMR)
    agent           — Grafo LangGraph con nodos de razonamiento y herramientas
    tools           — Herramientas del agente (búsqueda, predicción de precio, stats)
    utils           — Funciones auxiliares del agente (formateo, validación)

Punto de entrada:
    app.py          — Interfaz de chat interactiva en terminal o API
"""

"""
retriever.py
============
Estrategia de recuperación de documentos para el agente RAG.
Combina búsqueda semántica en ChromaDB con filtros estructurados sobre la BD
para mejorar la precisión de los resultados.

Estrategias implementadas:
    1. Semántica pura       — Búsqueda vectorial en ChromaDB (sin filtros)
    2. Híbrida              — Semántica + filtros de precio/ciudad/metros
    3. Re-ranking           — Re-ordena los candidatos con un LLM ligero
                             para seleccionar los más relevantes a la pregunta

Clase principal:
    InmuebleRetriever(BaseRetriever)
        - _get_relevant_documents(query) → List[Document]
        - Extrae filtros de la query con NER simple o un LLM
        - Combina resultados de ChromaDB y de la BD SQL

Uso:
    from 03_rag_agent.src.retriever import InmuebleRetriever
    retriever = InmuebleRetriever(k=5, ciudad="madrid", precio_max=1500)
    docs = retriever.get_relevant_documents("busco piso con 2 habitaciones")
"""

# TODO: from langchain.schema import BaseRetriever, Document
# TODO: from 03_rag_agent.src.vectorstore import buscar_con_filtros
# TODO: from src.database.crud import obtener_inmuebles

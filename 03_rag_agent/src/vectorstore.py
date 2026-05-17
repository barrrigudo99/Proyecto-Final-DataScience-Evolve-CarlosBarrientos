"""
vectorstore.py
==============
Wrapper sobre ChromaDB que expone una interfaz limpia para búsqueda semántica.
Centraliza la configuración del vector store y evita repetir código en otros módulos.

Funciones:
    obtener_vectorstore()           — Carga ChromaDB desde disco (debe existir el índice)
    buscar_similares(query, k)      — Búsqueda por similitud coseno, retorna k documentos
    buscar_con_filtros(query, filtros, k) — Búsqueda con filtros de metadata
                                           (ciudad, precio_max, metros_min, etc.)
    obtener_retriever(modo)         — Retorna un retriever LangChain
                                      modo: "similarity" | "mmr" (diversidad máxima)

Por qué MMR:
    Maximum Marginal Relevance evita recuperar documentos muy similares entre sí,
    mejorando la diversidad de los anuncios presentados al usuario.

Uso:
    from 03_rag_agent.src.vectorstore import obtener_retriever
    retriever = obtener_retriever(modo="mmr")
    docs = retriever.get_relevant_documents("pisos baratos en Valencia")
"""

# TODO: from langchain_community.vectorstores import Chroma
# TODO: from 03_rag_agent.src.embeddings import obtener_modelo_embeddings
# TODO: Chroma(persist_directory=..., embedding_function=...)

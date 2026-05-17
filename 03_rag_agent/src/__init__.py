"""
03_rag_agent.src
================
Módulos Python del agente RAG. Cada módulo tiene una responsabilidad única
siguiendo el principio de separación de concerns.

Flujo de datos:
    BD SQLite → document_loader → embeddings → vector_store (ChromaDB)
                                                     ↓
    Consulta usuario → retriever → agent (LangGraph) → tools → respuesta
"""

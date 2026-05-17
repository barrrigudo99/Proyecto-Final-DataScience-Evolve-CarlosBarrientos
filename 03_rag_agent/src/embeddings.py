"""
embeddings.py
=============
Genera y persiste los embeddings de los documentos de inmuebles en ChromaDB.
Debe ejecutarse una vez tras el scraping, o de forma incremental ante nuevos datos.

Modelo de embeddings:
    OpenAI text-embedding-3-small (1536 dimensiones, equilibrio coste/calidad)
    Configurable en config/config.yaml para cambiar a modelos locales (HuggingFace).

Funciones:
    generar_embeddings(documentos)      — Crea o actualiza el índice ChromaDB
    verificar_indice()                  — Comprueba que el índice está actualizado
    obtener_modelo_embeddings()         — Retorna el modelo configurado

Uso:
    python 03_rag_agent/src/embeddings.py        # Regenera índice completo
    python 03_rag_agent/src/embeddings.py --modo incremental
"""

# TODO: from langchain_openai import OpenAIEmbeddings
# TODO: from langchain_community.vectorstores import Chroma
# TODO: from 03_rag_agent.src.document_loader import cargar_documentos_desde_db
# TODO: persistir en config["datos"]["ruta_embeddings"]

"""
utils.py
========
Funciones auxiliares específicas del agente RAG.
Distintas de src/utils/ (que son genéricas del proyecto).

Funciones:
    formatear_anuncios(docs)        — Convierte List[Document] a texto legible para el LLM
    extraer_filtros_de_query(query) — Extrae ciudad, precio_max, metros de texto libre
                                      usando regex o un LLM ligero
    limpiar_historial(messages)     — Trunca el historial si supera el límite de tokens
    formatear_respuesta_final(texto)— Aplica formato markdown a la respuesta del agente

Uso:
    from 03_rag_agent.src.utils import formatear_anuncios, extraer_filtros_de_query
    texto = formatear_anuncios(docs_recuperados)
    filtros = extraer_filtros_de_query("quiero un piso en Sevilla por menos de 800€")
"""

# TODO: importar re, langchain.schema.Document
# TODO: regex para ciudades (lista predefinida), precios (€, euros), metros (m²)
# TODO: función limpiar_historial con tiktoken para contar tokens

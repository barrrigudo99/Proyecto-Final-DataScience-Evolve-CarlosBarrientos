"""
document_loader.py
==================
Convierte los registros de la base de datos de inmuebles en documentos
LangChain con metadata para indexar en ChromaDB.

Cada anuncio se convierte en un Document con:
    - page_content: descripción en texto natural del anuncio
      Ejemplo: "Piso de 3 habitaciones y 85m² en Malasaña, Madrid.
                Alquiler por 1.200€/mes. Incluye calefacción central."
    - metadata: dict con precio_mes, metros, ciudad, distrito, latitud,
                longitud, url_anuncio, fecha_scraping

Por qué texto natural en page_content:
    Los embeddings capturan semántica del texto; un formato narrativo
    produce mejores recuperaciones que un JSON serializado.

Funciones:
    inmueble_a_documento(fila)          — Convierte una fila del DF a Document
    cargar_documentos_desde_db()        — Carga todos los inmuebles de la BD
    cargar_documentos_incrementales()   — Solo los anuncios nuevos desde último run

Uso:
    from 03_rag_agent.src.document_loader import cargar_documentos_desde_db
    docs = cargar_documentos_desde_db()
"""

# TODO: from langchain.schema import Document
# TODO: from src.database.crud import obtener_inmuebles
# TODO: función inmueble_a_documento que genera texto natural coherente

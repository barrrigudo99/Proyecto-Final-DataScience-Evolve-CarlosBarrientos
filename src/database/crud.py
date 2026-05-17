"""
crud.py
=======
Operaciones CRUD (Create, Read, Update, Delete) sobre la base de datos.
Centraliza toda la lógica de persistencia para que los scrapers y el EDA
no escriban SQL directamente.

Funciones principales:
    insertar_inmuebles(df)          — Inserta un DataFrame limpio en la BD
    obtener_inmuebles(ciudad, ...)  — Consulta con filtros opcionales
    obtener_estadisticas_ciudad()   — Estadísticas agregadas por ciudad
    actualizar_precio(id, precio)   — Actualiza el precio de un anuncio
    eliminar_duplicados()           — Elimina registros con URL duplicada

Uso:
    from src.database.crud import insertar_inmuebles, obtener_inmuebles
    insertar_inmuebles(df_limpio)
    df = obtener_inmuebles(ciudad="madrid", precio_max=1500)
"""

# TODO: importar Session, Inmueble, pandas
# TODO: función insertar_inmuebles(df, session) con upsert por url_anuncio
# TODO: función obtener_inmuebles(session, ciudad=None, precio_max=None, ...) → DataFrame
# TODO: función obtener_estadisticas_ciudad(session) → dict con media, mediana, percentiles

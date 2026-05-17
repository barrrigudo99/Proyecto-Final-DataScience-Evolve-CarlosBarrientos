"""
data_cleaning.py
================
Limpieza y unificación de los CSV/JSON crudos producidos por los scrapers.
Convierte los tres ficheros raw en un único DataFrame limpio que se persiste
en data/processed/inmuebles_clean.csv y en la base de datos SQLite.

Operaciones:
    - Renombrar columnas a un esquema unificado
    - Parsear precios: eliminar "€", "/mes", separadores de miles → float
    - Parsear metros: extraer número de strings como "85 m²" → float
    - Eliminar duplicados por URL de anuncio
    - Detectar y tratar outliers de precio (IQR o percentiles)
    - Geocodificar direcciones faltantes (opcional, vía Nominatim)
    - Guardar en SQLite mediante src/database/crud.py

Uso:
    python 00_scraping/data_cleaning.py
    python 00_scraping/data_cleaning.py --input data/raw/ --output data/processed/
"""

# TODO: importar pandas, sqlite3, loguru, src.database.crud
# TODO: función unificar_fuentes(ruta_raw) → DataFrame
# TODO: función limpiar_precios(df) → DataFrame
# TODO: función eliminar_duplicados(df) → DataFrame
# TODO: función guardar_procesado(df, ruta_db)

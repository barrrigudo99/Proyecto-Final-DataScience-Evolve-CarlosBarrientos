"""
run_scrapers.py
===============
Orquestador del pipeline de scraping. Ejecuta los scrapers en secuencia,
llama a data_cleaning.py y registra el resultado en los logs.

Orden de ejecución:
    1. IdealistaScraper  → data/raw/idealista_raw.csv
    2. PisosScraper      → data/raw/pisos_raw.csv
    3. FotocasaScraper   → data/raw/fotocasa_raw.json  (vía subprocess Node.js)
    4. data_cleaning     → data/processed/inmuebles_clean.csv + SQLite

Puede ejecutarse manualmente o programarse con cron / Airflow.

Uso:
    python 00_scraping/run_scrapers.py
    python 00_scraping/run_scrapers.py --solo idealista
    python 00_scraping/run_scrapers.py --ciudad madrid --max-paginas 10
"""

# TODO: importar los scrapers y data_cleaning
# TODO: argparse con opciones --solo, --ciudad, --max-paginas
# TODO: logging de inicio/fin de cada etapa con duración y nº de registros
# TODO: manejo de errores: si un scraper falla, continúa con el siguiente

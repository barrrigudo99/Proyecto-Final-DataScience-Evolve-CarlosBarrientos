"""
idealista_scraper.py
====================
Extrae anuncios de alquiler de Idealista.com usando Playwright para
manejar el renderizado JavaScript y la paginación dinámica.

Flujo:
    1. Lanza un navegador headless con Playwright
    2. Itera sobre ciudades definidas en config/config.yaml
    3. Navega por páginas de resultados y extrae campos de cada anuncio
    4. Guarda el resultado en data/raw/idealista_raw.csv

Campos extraídos:
    titulo, precio_mes, metros, habitaciones, planta, ciudad,
    distrito, direccion, url_anuncio, fecha_scraping

Uso:
    python 00_scraping/idealista_scraper.py
    python 00_scraping/idealista_scraper.py --ciudad madrid --max-paginas 5
"""

# TODO: importar Playwright, pandas, loguru, config
# TODO: clase IdealistaScraper con métodos scrape_ciudad() y guardar_csv()
# TODO: main() con argparse para --ciudad y --max-paginas

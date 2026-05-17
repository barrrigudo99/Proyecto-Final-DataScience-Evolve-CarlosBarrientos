"""
pisos_scraper.py
================
Extrae anuncios de alquiler de Pisos.com usando requests + BeautifulSoup.
Pisos.com renderiza HTML estático, por lo que no necesita Playwright.

Flujo:
    1. Construye URLs de búsqueda por ciudad
    2. Descarga el HTML con requests y parsea con BeautifulSoup
    3. Extrae los campos del listado y de cada ficha de anuncio
    4. Guarda en data/raw/pisos_raw.csv

Campos extraídos:
    titulo, precio_mes, metros, habitaciones, ciudad,
    barrio, caracteristicas, url_anuncio, fecha_scraping

Uso:
    python 00_scraping/pisos_scraper.py
"""

# TODO: importar requests, BeautifulSoup, pandas, loguru
# TODO: clase PisosScraper con métodos get_listado() y parsear_anuncio()
# TODO: lógica de reintentos con backoff exponencial ante errores HTTP 429

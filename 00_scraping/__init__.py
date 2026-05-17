"""
Paquete 00_scraping
===================
Contiene los scrapers para extraer anuncios de alquiler de los principales
portales inmobiliarios españoles. Cada módulo es independiente y produce
un CSV crudo que se almacena en data/raw/.

Módulos:
    idealista_scraper  — Extracción de Idealista.com
    fotocasa_scraper   — Extracción de Fotocasa.es
    pisos_scraper      — Extracción de Pisos.com
    data_cleaning      — Limpieza inicial y unificación de los CSV crudos
    run_scrapers       — Orquestador: ejecuta todos los scrapers en secuencia
"""

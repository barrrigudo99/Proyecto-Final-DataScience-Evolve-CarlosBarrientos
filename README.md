# Análisis del Mercado de Alquiler en España

Proyecto de Data Science, Machine Learning y RAG aplicado al mercado de alquiler residencial español.
Fuentes de datos: portales inmobiliarios (Idealista, Fotocasa, Pisos.com).

---

## Objetivo

Construir un pipeline completo que:
1. **Extrae** datos de alquiler de portales inmobiliarios (`00_scraping/`)
2. **Analiza** el mercado con visualizaciones y estadísticas (`01_eda_analysis/`)
3. **Predice** precios de alquiler con modelos de ML (`02_ml_models/`)
4. **Responde** preguntas en lenguaje natural sobre el mercado mediante un agente RAG (`03_rag_agent/`)

---

## Estructura del Proyecto

```
├── 00_scraping/          # Extracción de datos de portales inmobiliarios
├── 01_eda_analysis/      # Análisis exploratorio y visualizaciones
├── 02_ml_models/         # Modelos de predicción de precios
├── 03_rag_agent/         # Agente RAG con LangGraph para consultas en lenguaje natural
├── src/                  # Código reutilizable (DB, preprocesado, utilidades)
├── config/               # Configuración centralizada (YAML)
├── data/                 # Datos raw, procesados y embeddings
├── logs/                 # Registros de ejecución
└── docs/                 # Documentación del proyecto
```

---

## Instalación

```bash
python -m venv entorno
source entorno/bin/activate      # Linux/Mac
# entorno\Scripts\activate       # Windows

pip install -r requirements.txt
cp .env.example .env             # Rellenar con tus claves API
```

---

## Flujo de Ejecución

```
python 00_scraping/run_scrapers.py        # 1. Scraping
jupyter notebook 01_eda_analysis/         # 2. EDA
jupyter notebook 02_ml_models/            # 3. ML
python 03_rag_agent/app.py                # 4. Agente RAG
```

---

## Tecnologías

| Área        | Herramientas                              |
|-------------|-------------------------------------------|
| Scraping    | Playwright, BeautifulSoup, Selenium, PostgreSQL         |
| EDA         | Pandas, Seaborn, Plotly                   |
| ML          | Scikit-learn, XGBoost, LightGBM           |
| RAG / Agent | LangChain, LangGraph, ChromaDB, OpenAI    |

---

## Base de Datos

PostgreSQL (`data/processed/inmuebles.db`) — tabla principal: `inmuebles`

| Campo          | Tipo    | Descripción                        |
|----------------|---------|------------------------------------|
| id             | INTEGER | Clave primaria                     |
| titulo         | TEXT    | Título del anuncio                 |
| precio_mes     | REAL    | Precio mensual en euros            |
| metros         | REAL    | Superficie en m²                   |
| habitaciones   | INTEGER | Número de habitaciones             |
| ciudad         | TEXT    | Ciudad                             |
| distrito       | TEXT    | Distrito o barrio                  |
| latitud        | REAL    | Coordenada geográfica              |
| longitud       | REAL    | Coordenada geográfica              |
| fuente         | TEXT    | Portal de origen (idealista, etc.) |
| fecha_scraping | DATE    | Fecha de extracción                |

---

*Proyecto Final — Master Data Science & IA — Evolve*

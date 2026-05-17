# Análisis e Insights del Mercado de Alquiler en España con IA

##  Título y Descripción

**Problema:** El mercado de alquiler en España es fragmentado, con información dispersa en múltiples portales y búsquedas rígidas que no captan consultas flexibles en lenguaje natural.

**Solución:** Un pipeline end-to-end que:
1. **Extrae** datos de portales inmobiliarios (scraping automatizado)
2. **Analiza** patrones y correlaciones del mercado (EDA)
3. **Predice** precios con modelos de machine learning
4. **Responde** consultas en lenguaje natural sobre el mercado mediante un agente RAG inteligente

**Enfoque:** Combinamos técnicas clásicas de data science (EDA, ML) con inteligencia artificial moderna (RAG, LLMs) para crear un asistente que entiende preguntas como *"¿Qué hay barato en Malasaña?"* o *"Zona tranquila bien comunicada"*.

---

##  Tecnologías y Herramientas

### Lenguajes y Librerías Core
- **Python 3.9+** — Lenguaje principal
- **Pandas, NumPy** — Manipulación y análisis de datos
- **Scikit-learn** — Modelos de ML (regresión, clasificación, árboles)

### Scraping y Data Collection
- **BeautifulSoup, Requests** — HTML parsing estático
- **Playwright, Selenium** — Navegación y JS dinámico
- **Node.js + Puppeteer** — Scraping avanzado anti-bot

### Análisis Exploratorio (EDA)
- **Matplotlib, Seaborn** — Visualizaciones estáticas
- **Plotly** — Gráficos interactivos
- **Folium** — Mapas geográficos

### Machine Learning y Predicción
- **XGBoost, LightGBM** — Modelos de predicción de precios
- **SHAP** — Interpretabilidad de modelos

### RAG e Inteligencia Artificial
- **LangChain, LangGraph** — Orquestación de agentes
- **ChromaDB** — Base de datos vectorial
- **Sentence-Transformers** — Embeddings locales
- **OpenAI API** — LLM para generación de respuestas

### Base de Datos y Storage
- **PostgreSQL** — Base de datos relacional para datos crudos scrapeados (inmuebles_raw)
- **ChromaDB** — Base de datos vectorial para embeddings y búsqueda semántica RAG

### Herramientas Auxiliares
- **Jupyter Notebooks** — Desarrollo interactivo
- **Git** — Control de versiones
- **Loguru** — Logging estructurado
- **Python-dotenv** — Gestión de variables de entorno

---

##  Estructura del Repositorio

```
Proyecto-Final-DataScience-Evolve-CarlosBarrientos/

├── 00_scraping/
│   ├── fotocasa_scraper.js          ← Script Node.js: extrae anuncios de Fotocasa
│   ├── idealista_scraper.py         ← Python: scraping dinámico con Playwright
│   ├── pisos_scraper.py             ← Python: parsing HTML estático
│   ├── data_cleaning.py             ← Limpieza y normalización de datos crudos
│   ├── run_scrapers.py              ← Orquestador: ejecuta todos los scrapers
│   └── README_scraping.md           ← Documentación del módulo
│
├── 01_eda_analysis/
│   ├── 01_exploracion_datos.ipynb   ← EDA completo: distribuciones, correlaciones, outliers
│   ├── 02_visualizaciones.ipynb     ← Gráficos: histogramas, scatter, mapas, heatmaps
│   └── output/                      ← Salida: PNGs, HTMLs interactivos
│
├── 02_ml_models/
│   ├── 03_regresion_precios.ipynb   ← Entrenamiento: RF, XGBoost, LightGBM
│   ├── 04_analisis_features.ipynb   ← Feature importance, SHAP, análisis de errores
│   ├── train.py                     ← Script de entrenamiento en producción
│   ├── predict.py                   ← Inferencia (usado por agente RAG)
│   ├── model_evaluation.md          ← Registro de métricas
│   └── models/                      ← Modelos entrenados (.pkl, .joblib)
│
├── 03_rag_agent/
│   ├── 05_rag_setup.ipynb           ← Construcción del índice ChromaDB
│   ├── 06_agente_langgraph.ipynb    ← Desarrollo y pruebas del agente
│   ├── app.py                       ← CLI interactivo: chat con el agente
│   ├── queries_examples.txt         ← Ejemplos de consultas por complejidad
│   ├── README_rag.md                ← Documentación del módulo
│   └── src/
│       ├── document_loader.py       ← Carga BD → documentos en texto natural
│       ├── embeddings.py            ← Genera embeddings con Sentence-Transformers
│       ├── vectorstore.py           ← Gestor ChromaDB: búsqueda MMR
│       ├── retriever.py             ← Recuperación: búsqueda semántica + filtros
│       ├── tools.py                 ← Herramientas del agente (5 funciones)
│       ├── agent.py                 ← Lógica LangGraph: ciclo ReAct
│       └── utils.py                 ← Funciones auxiliares: parsing, formateo
│
├── src/
│   ├── database/
│   │   ├── connection.py            ← Conexión a inmuebles.db (SQLite/PostgreSQL)
│   │   ├── models.py                ← Definición de tablas (SQLAlchemy)
│   │   └── crud.py                  ← Operaciones CRUD
│   ├── preprocessing/
│   │   ├── cleaner.py               ← Limpieza de datos (normalización, outliers)
│   │   ├── normalizer.py            ← Normalización de formatos
│   │   └── feature_extractor.py     ← Feature engineering
│   └── utils/
│       ├── logger.py                ← Setup de logging centralizado
│       └── helpers.py               ← Funciones auxiliares comunes
│
├── config/
│   ├── config.yaml                  ← Configuración: ciudades, delays, rutas
│   ├── database.yaml                ← Conexión BD: SQLite/PostgreSQL
│   └── model_params.yaml            ← Hiperparámetros y features del modelo
│
├── data/
│   ├── raw/                         ← CSVs del scraping (temporal, ignorados en Git)
│   ├── processed/                   ← PostgreSQL inmuebles_raw (datos crudos)
│   └── embeddings/                  ← ChromaDB (índice vectorial para RAG)
│
├── logs/                            ← Archivos de log con rotación
│
├── docs/
│   ├── ARQUITECTURA.md              ← Diagrama de componentes y flujos
│   ├── METODOLOGIA.md               ← Decisiones técnicas (CRISP-DM adaptado)
│   └── RESULTADOS_CLAVE.md          ← Tabla de métricas (para rellenar)
│
├── .gitignore                       ← Exclusiones: datos, modelos, logs, .env
├── .env.example                     ← Plantilla de variables de entorno
├── requirements.txt                 ← Dependencias Python agrupadas por módulo
└── README.md                        ← Este archivo

```

### Descripción por Carpeta

| Carpeta | Contenido | Propósito |
|---------|----------|-----------|
| `00_scraping/` | Scripts de extracción (JS, Python) | Obtener 21K+ registros de portales inmobiliarios |
| `01_eda_analysis/` | Notebooks de análisis | Entender distribuciones, correlaciones, patrones |
| `02_ml_models/` | Notebooks y scripts de ML | Entrenar modelos de predicción de precios |
| `03_rag_agent/` | Notebooks, app CLI, módulos RAG | Crear agente inteligente que responde en lenguaje natural |
| `src/` | Código reutilizable | Funciones comunes (BD, preprocesado, logging) |
| `config/` | Archivos YAML | Centralizar configuración (parámetros, credenciales) |
| `data/` | Raw (CSV), PostgreSQL, ChromaDB | Almacenamiento: datos crudos en PostgreSQL, embeddings en ChromaDB |
| `logs/` | Registros de ejecución | Debugging y monitoreo |
| `docs/` | Documentación técnica | Explicar arquitectura, decisiones, resultados |

---

**Proyecto Final — Master en Data Science de Evolve**

**Enlaces a documentación sobre el proyecto:**
- medium --> https://medium.com/@carlosbarrientoslopez/cuando-los-datos-te-cuentan-historias-analisis-del-mercado-inmobiliario-español-con-ia-4d51a4a07ac0
- dev.to --> https://dev.to/carlos_barrientos_6d15639/analisis-del-mercado-de-alquiler-en-espana-scraping-ml-e-ia-con-llms-locales-49hc
- linkedin --> https://www.linkedin.com/feed/update/urn:li:activity:7461840870833758209/



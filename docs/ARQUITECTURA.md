# Arquitectura del Proyecto

Descripción de la arquitectura técnica del sistema de análisis del mercado de alquiler.

---

## Visión General

```
┌──────────────────────────────────────────────────────────────────┐
│                     FUENTES DE DATOS                             │
│  Idealista.com  │  Fotocasa.es  │  Pisos.com                     │
└────────┬─────────────────┬────────────────┬─────────────────────┘
         │                 │                │
         ▼                 ▼                ▼
┌──────────────────────────────────────────────────────────────────┐
│                    00_scraping/                                   │
│  idealista_scraper.py  fotocasa_scraper.js  pisos_scraper.py     │
│                    data_cleaning.py                               │
└──────────────────────────┬───────────────────────────────────────┘
                           │  data/raw/*.csv
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│              src/preprocessing/  +  src/database/                │
│  cleaner → normalizer → feature_extractor → SQLite (inmuebles)   │
└──────────────────────────┬───────────────────────────────────────┘
              ┌────────────┼────────────┐
              ▼            ▼            ▼
      ┌───────────┐ ┌───────────┐ ┌──────────────────┐
      │ 01_eda_   │ │ 02_ml_    │ │  03_rag_agent/   │
      │ analysis/ │ │ models/   │ │  ChromaDB +       │
      │ notebooks │ │ XGBoost   │ │  LangGraph Agent  │
      └───────────┘ └───────────┘ └──────────────────┘
```

---

## Componentes Principales

### 1. Pipeline de Scraping (`00_scraping/`)
- **Tecnología:** Playwright (JS dinámico), BeautifulSoup (HTML estático), Node.js/Puppeteer
- **Salida:** CSV/JSON en `data/raw/`
- **Frecuencia:** Manual o programado con cron

### 2. Capa de Datos (`src/database/`)
- **Motor:** SQLite (desarrollo) → PostgreSQL (producción)
- **ORM:** SQLAlchemy con modelos declarativos
- **Tabla principal:** `inmuebles` (~50K registros esperados)

### 3. Preprocesado (`src/preprocessing/`)
- **Flujo:** raw CSV → limpieza → normalización → features → SQLite
- **Pipeline:** ColumnTransformer de scikit-learn (reutilizable entre train/test)

### 4. Modelos ML (`02_ml_models/`)
- **Target:** precio_mes (regresión)
- **Modelo ganador:** Por determinar (XGBoost o LightGBM esperado)
- **Artefacto:** `models/mejor_modelo.pkl`

### 5. Agente RAG (`03_rag_agent/`)
- **Vector store:** ChromaDB local
- **Embeddings:** OpenAI text-embedding-3-small
- **LLM:** GPT-4o-mini (balance coste/razonamiento)
- **Orquestación:** LangGraph con ciclo ReAct

---

## Decisiones Técnicas

| Decisión | Alternativa rechazada | Motivo |
|----------|----------------------|--------|
| SQLite | PostgreSQL | Simplicidad para proyecto académico |
| ChromaDB | Pinecone, Weaviate | Local, sin costes de API |
| LangGraph | LangChain LCEL | Mejor manejo de estado y ciclos |
| text-embedding-3-small | text-embedding-ada-002 | Mejor calidad, mismo coste |

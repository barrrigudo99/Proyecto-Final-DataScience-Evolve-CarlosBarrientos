# Metodología del Proyecto

Descripción del proceso seguido y las decisiones metodológicas tomadas.

---

## Metodología de Data Science

Seguimos el proceso estándar **CRISP-DM** adaptado al proyecto:

### 1. Comprensión del Negocio
- **Problema:** El mercado de alquiler español es opaco; los inquilinos carecen de
  herramientas para evaluar si un precio es justo para su zona.
- **Objetivo:** Predecir precios y permitir consultas en lenguaje natural.
- **KPIs de éxito:** MAE < 150€, R² > 0.80, agente responde correctamente >80% de queries.

### 2. Comprensión de los Datos
- Fuentes: tres portales inmobiliarios (Idealista, Fotocasa, Pisos.com)
- Variables clave: precio_mes, metros, habitaciones, ciudad, distrito, coordenadas
- Periodo de datos: pendiente de scraping
- Ver: `01_eda_analysis/01_exploracion_datos.ipynb`

### 3. Preparación de los Datos
- Unificación de tres fuentes heterogéneas → esquema común
- Limpieza de precios, metros y texto libre
- Eliminación de duplicados por URL
- Feature engineering: precio/m², distancia al centro, zonas premium
- Ver: `src/preprocessing/`, `00_scraping/data_cleaning.py`

### 4. Modelado
- Comparación de tres modelos de regresión (RF, XGBoost, LightGBM)
- Validación cruzada 5-fold para robustez
- Selección por MAE y R² en conjunto de test
- Ver: `02_ml_models/03_regresion_precios.ipynb`

### 5. Evaluación
- Métricas: MAE, RMSE, R²
- Análisis de errores por ciudad y tipo de inmueble
- Interpretabilidad con SHAP
- Ver: `02_ml_models/04_analisis_features.ipynb`, `model_evaluation.md`

### 6. Despliegue
- Modelo serializado como `.pkl` para consumo desde el agente RAG
- Agente RAG accesible vía CLI (`app.py`)

---

## Metodología del Sistema RAG

### Construcción del Índice
1. Convertir cada anuncio a texto natural descriptivo (evita JSON serializado)
2. Generar embeddings con OpenAI text-embedding-3-small
3. Persistir en ChromaDB con metadata filtrables (ciudad, precio, metros)

### Estrategia de Recuperación
- **Por defecto:** MMR (Maximum Marginal Relevance) con k=5
- **Con filtros:** Búsqueda híbrida semántica + filtros de metadata

### Evaluación del RAG
- Métricas: Faithfulness, Answer Relevancy, Context Precision
- Framework: RAGAS (pendiente de implementar)

---

## Reproducibilidad

- Semillas fijas: `random_state=42` en todos los modelos
- Versiones de paquetes: `requirements.txt` con versiones exactas
- Configuración centralizada: `config/` para evitar valores hardcodeados

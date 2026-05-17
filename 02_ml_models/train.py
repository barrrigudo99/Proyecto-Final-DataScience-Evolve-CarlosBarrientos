"""
train.py
========
Script de entrenamiento del modelo de predicción de precios en modo producción.
Lee los datos limpios, aplica el pipeline de preprocesado, entrena el modelo
con los mejores hiperparámetros y lo serializa para inferencia posterior.

Diferencia con el notebook:
    El notebook es exploratorio (comparación de modelos).
    Este script entrena directamente el modelo ganador con el dataset completo.

Flujo:
    1. Carga datos desde SQLite (src/database/crud.py)
    2. Aplica feature engineering (src/preprocessing/feature_extractor.py)
    3. Construye pipeline de preprocesado (src/preprocessing/normalizer.py)
    4. Lee hiperparámetros desde config/model_params.yaml
    5. Entrena con validación cruzada y loggea métricas
    6. Serializa modelo + pipeline en 02_ml_models/models/modelo_v{version}.pkl

Uso:
    python 02_ml_models/train.py
    python 02_ml_models/train.py --modelo xgboost --version 2
"""

# TODO: importar sklearn, xgboost, joblib, src.database.crud, src.preprocessing.*
# TODO: argparse para --modelo y --version
# TODO: logging de métricas (MAE, RMSE, R²) al finalizar el entrenamiento

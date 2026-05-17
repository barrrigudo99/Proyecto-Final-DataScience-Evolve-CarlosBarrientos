"""
normalizer.py
=============
Escalado y codificación de variables para preparar el DataFrame para ML.
Usa sklearn para mantener consistencia entre train y test/producción.

Funciones:
    crear_pipeline_preprocesado()   — Retorna un ColumnTransformer de sklearn
                                      con StandardScaler para numéricas y
                                      OneHotEncoder para categóricas
    ajustar_y_transformar(df)       — Ajusta el pipeline y transforma train
    transformar(df)                 — Aplica el pipeline ya ajustado a test

Uso:
    from src.preprocessing.normalizer import crear_pipeline_preprocesado
    pipeline = crear_pipeline_preprocesado()
    X_train = pipeline.fit_transform(df_train)
    X_test  = pipeline.transform(df_test)
"""

# TODO: from sklearn.pipeline import Pipeline
# TODO: from sklearn.preprocessing import StandardScaler, OneHotEncoder
# TODO: from sklearn.compose import ColumnTransformer
# TODO: leer features de config/model_params.yaml

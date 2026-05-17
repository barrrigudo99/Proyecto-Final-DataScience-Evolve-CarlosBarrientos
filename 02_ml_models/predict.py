"""
predict.py
==========
Carga el modelo entrenado y genera predicciones de precio para nuevos anuncios.
Usado por el agente RAG (03_rag_agent/src/tools.py) como herramienta de
estimación de precio en tiempo real.

Funciones:
    cargar_modelo(ruta)             — Deserializa el pipeline + modelo guardado
    predecir_precio(inmueble_dict)  — Predicción individual → float (€/mes)
    predecir_batch(df)              — Predicciones para un DataFrame completo

Uso:
    from 02_ml_models.predict import predecir_precio
    precio = predecir_precio({"metros": 80, "habitaciones": 3, "ciudad": "madrid", ...})

    python 02_ml_models/predict.py --input data/raw/nuevos_anuncios.csv
"""

# TODO: importar joblib, pandas
# TODO: cargar automáticamente el modelo más reciente de models/
# TODO: validar que el dict de entrada tenga todas las features necesarias

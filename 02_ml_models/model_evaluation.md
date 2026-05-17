# Evaluación de Modelos — Mercado de Alquiler España

Registro de métricas de cada experimento de entrenamiento.
Actualizar manualmente tras cada run de `train.py` o al finalizar el notebook `03_regresion_precios.ipynb`.

---

## Métricas

| Modelo          | MAE (€) | RMSE (€) | R²   | CV R² (±std) | Fecha      | Notas                        |
|-----------------|---------|----------|------|--------------|------------|------------------------------|
| Baseline Lineal | —       | —        | —    | —            | pendiente  | Referencia mínima            |
| Random Forest   | —       | —        | —    | —            | pendiente  | 200 árboles, depth=15        |
| XGBoost         | —       | —        | —    | —            | pendiente  | lr=0.05, 300 estimadores     |
| LightGBM        | —       | —        | —    | —            | pendiente  | num_leaves=63                |

---

## Definición de Métricas

- **MAE** — Error Absoluto Medio en euros. Interpretable directamente: "el modelo se equivoca de media X€/mes".
- **RMSE** — Raíz del Error Cuadrático Medio. Penaliza más los errores grandes.
- **R²** — Varianza explicada. 1.0 = predicción perfecta.
- **CV R²** — R² promedio en 5-fold cross-validation ± desviación estándar.

---

## Modelo Seleccionado

> Pendiente de completar tras los experimentos.

**Modelo:** —  
**Ruta:** `02_ml_models/models/mejor_modelo.pkl`  
**Justificación:** —

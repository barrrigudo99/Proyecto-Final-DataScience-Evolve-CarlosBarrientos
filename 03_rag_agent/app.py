"""
app.py
======
Punto de entrada de la aplicación del agente RAG.
Ofrece dos modos de uso:
    1. CLI interactivo — Chat en terminal con historial de conversación
    2. API (futuro)    — Endpoint /chat para integrar en una web

Inicialización:
    - Verifica que el índice ChromaDB existe (si no, lo genera)
    - Verifica que el modelo ML está disponible en 02_ml_models/models/
    - Compila el grafo LangGraph del agente
    - Inicia el bucle de conversación

Uso:
    python 03_rag_agent/app.py                  # Modo CLI interactivo
    python 03_rag_agent/app.py --demo           # Ejecuta queries de ejemplo
    python 03_rag_agent/app.py --query "¿Cuánto cuesta alquilar en Málaga?"
"""

# TODO: importar agent.crear_agente, embeddings.verificar_indice, loguru
# TODO: bucle while True con input() y manejo de KeyboardInterrupt
# TODO: argparse para --demo y --query
# TODO: mostrar el pensamiento del agente (steps) en modo verbose

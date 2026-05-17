"""
agent.py
========
Grafo LangGraph del agente inteligente para consultas sobre el mercado de alquiler.
Implementa un ciclo de razonamiento ReAct (Reason + Act) con estado persistente.

Nodos del grafo:
    ┌─────────────┐
    │  __start__  │
    └──────┬──────┘
           │
    ┌──────▼──────┐     ┌───────────────┐
    │   razonar   │────►│  ejecutar_tool │
    │   (LLM)     │◄────│  (tools.py)   │
    └──────┬──────┘     └───────────────┘
           │ (respuesta final)
    ┌──────▼──────┐
    │   __end__   │
    └─────────────┘

Estado del grafo (AgentState):
    messages  — Historial de mensajes (HumanMessage, AIMessage, ToolMessage)
    pasos     — Número de iteraciones del ciclo para evitar loops infinitos

Configuración:
    LLM:    GPT-4o-mini (balance coste/razonamiento para preguntas inmobiliarias)
    Tools:  Las definidas en tools.py
    Límite: max 10 iteraciones por consulta

Uso:
    from 03_rag_agent.src.agent import crear_agente
    agente = crear_agente()
    respuesta = agente.invoke({"messages": [HumanMessage("¿Cuánto cuesta alquilar en Madrid?")]})
"""

# TODO: from langgraph.graph import StateGraph, END
# TODO: from langgraph.prebuilt import ToolNode
# TODO: from langchain_openai import ChatOpenAI
# TODO: from 03_rag_agent.src.tools import buscar_anuncios, estadisticas_mercado, predecir_precio
# TODO: definir AgentState como TypedDict con messages y pasos
# TODO: función crear_agente() que compila el grafo

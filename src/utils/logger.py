"""
logger.py
=========
Configura loguru como logger único para todo el proyecto.
Se importa una sola vez al inicio de cada script principal.

Comportamiento:
    - Escribe en consola (INFO+) y en logs/proyecto.log (DEBUG+)
    - Rotación automática del archivo de log al llegar a 10 MB
    - Formato: timestamp | nivel | módulo:línea | mensaje

Uso:
    from src.utils.logger import logger
    logger.info("Iniciando scraping de Idealista...")
    logger.error("Error al conectar: {error}", error=str(e))
"""

# TODO: from loguru import logger
# TODO: logger.remove()  → eliminar handler por defecto
# TODO: logger.add(sys.stderr, level="INFO", format=...)
# TODO: logger.add("logs/proyecto.log", level="DEBUG", rotation="10 MB", ...)
# TODO: exponer el logger configurado para importación

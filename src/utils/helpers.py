"""
helpers.py
==========
Funciones auxiliares reutilizables en múltiples partes del proyecto.

Funciones:
    load_config(ruta)           — Lee un YAML y retorna un dict
    get_project_root()          — Retorna el Path absoluto a la raíz del proyecto
    crear_directorios()         — Crea data/, logs/ si no existen
    timer(func)                 — Decorador que mide y loggea el tiempo de ejecución
    df_info_rapido(df)          — Imprime shape, dtypes y % de nulos de un DataFrame

Uso:
    from src.utils.helpers import load_config, timer
    cfg = load_config("config/config.yaml")
    ciudades = cfg["scraping"]["ciudades"]
"""

# TODO: importar yaml, pathlib.Path, time, functools, pandas
# TODO: load_config usa yaml.safe_load para no ejecutar código arbitrario
# TODO: get_project_root detecta la raíz buscando README.md hacia arriba
# TODO: timer como decorador con wraps para preservar el nombre de la función

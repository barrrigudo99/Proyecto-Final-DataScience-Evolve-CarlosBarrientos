"""
connection.py
=============
Gestiona la conexión a la base de datos mediante SQLAlchemy.
Lee la URL de conexión desde config/database.yaml o desde la variable
de entorno DATABASE_URL definida en .env.

Exporta:
    engine      — Motor SQLAlchemy (sqlite o postgresql)
    SessionLocal — Fábrica de sesiones para uso con context manager
    get_db()    — Generador de sesiones (compatible con FastAPI si se añade)

Uso:
    from src.database.connection import SessionLocal
    with SessionLocal() as db:
        resultados = db.query(Inmueble).filter(...).all()
"""

# TODO: importar sqlalchemy, dotenv, helpers.load_config
# TODO: crear engine según config/database.yaml
# TODO: SessionLocal = sessionmaker(bind=engine)
# TODO: función get_db() como generador de contexto

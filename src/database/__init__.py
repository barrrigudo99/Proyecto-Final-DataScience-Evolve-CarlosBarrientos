"""
src.database
============
Capa de acceso a datos. Abstrae la base de datos SQLite (o PostgreSQL)
del resto del proyecto para que los scrapers, el EDA y el ML no necesiten
escribir SQL directamente.

Módulos:
    connection  — Crea y gestiona la sesión SQLAlchemy
    models      — Define las tablas como clases ORM (declarative_base)
    crud        — Operaciones de lectura/escritura sobre las tablas
"""

"""
models.py
=========
Define el esquema de la base de datos como clases ORM de SQLAlchemy.
Cualquier cambio en la estructura de la tabla debe hacerse aquí.

Tablas:
    Inmueble  — Anuncio de alquiler (tabla principal)
    Ciudad    — Catálogo normalizado de ciudades con coordenadas
    Distrito  — Catálogo normalizado de distritos por ciudad

Relaciones:
    Inmueble.ciudad_id  → Ciudad.id  (many-to-one)
    Inmueble.distrito_id → Distrito.id (many-to-one)

Uso:
    from src.database.models import Base, Inmueble
    Base.metadata.create_all(engine)   # Crea las tablas si no existen
"""

# TODO: from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
# TODO: from sqlalchemy.orm import declarative_base, relationship
# TODO: Base = declarative_base()
# TODO: class Inmueble(Base): __tablename__ = "inmuebles" + columnas
# TODO: class Ciudad(Base): __tablename__ = "ciudades" + columnas
# TODO: class Distrito(Base): __tablename__ = "distritos" + columnas

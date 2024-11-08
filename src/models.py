import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    
class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favoritos_personajes(Base):
    __tablename__ = 'favoritos_personajes'
    id = Column(Integer, primary_key=True, nullable=False)
    personajes_relacion = Column(Integer, ForeignKey(Personajes.id), nullable=False)
    usuarios_relacion = Column(Integer, ForeignKey(Usuarios.id), nullable=False)

class Favoritos_vehiculos(Base):
    __tablename__ = 'favoritos_vehiculos'
    id = Column(Integer, primary_key=True, nullable=False)
    vehiculos_relacion = Column(Integer, ForeignKey(Vehiculos.id), nullable=False)
    usuarios_relacion = Column(Integer, ForeignKey(Usuarios.id), nullable=False)
    
class Favoritos_planetas(Base):
    __tablename__ = 'favoritos_planetas'
    id = Column(Integer, primary_key=True, nullable=False)
    planetas_relacion = Column(Integer, ForeignKey(Planetas.id), nullable=False)
    usuarios_relacion = Column(Integer, ForeignKey(Usuarios.id), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

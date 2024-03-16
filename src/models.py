import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    pasajeros = Column(Integer, nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehiculos_id = Column(Integer, ForeignKey('veiculos.id'))
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer, nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    pasajeros = Column(Integer, nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

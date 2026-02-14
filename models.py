#Mapeo de las tablas 

from flask_sqlalchemy import SQLAlchemy

import datetime

db=SQLAlchemy()
class Alumnos(db.Model):
    _tablename_='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now) #cada ves que hay una insercion dice la fecha

# Cada una de esta clases hacereferencia a las tablas de la base de datos
#Nombre de mi tabla = alumnos y sus campos son id que es primary key y auto incrementabe
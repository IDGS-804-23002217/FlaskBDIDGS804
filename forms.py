from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import validators
from wtforms.fields import EmailField, HiddenField
from wtforms.validators import DataRequired, Length, Email, NumberRange
 
class UserForm(FlaskForm):
    id = IntegerField('id', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])
   
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
   
    apellidos = StringField('apellidos', [
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email = EmailField('correo', [
        validators.DataRequired(message='El apellido es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])

    telefono = StringField('telefono', [
    validators.DataRequired(message='El teléfono es requerido'),
    ])

class MaestroForm(FlaskForm):
    matricula = HiddenField()   
    
    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(message='El nombre es requerido'),
            Length(min=4, max=20, message='Debe tener entre 4 y 20 caracteres')
        ]
    )
    apellidos = StringField(
        'Apellido',
        validators=[
            DataRequired(message='El apellido es requerido')
        ]
    )
    especialidad = StringField(
        'Especialidad',
        validators=[
            DataRequired(message='La especialidad es requerida')
        ]
    )
    email = EmailField(
        'Correo',
        validators=[
            DataRequired(message='El correo es requerido'),
            Email(message='Ingrese un correo válido')
        ]
    )
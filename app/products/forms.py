from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

#Formulario de registro

#de nuevo producto

class NewProductForm(FlaskForm):

    nombre = StringField(validators =[ InputRequired(message="nombre requerido") ],
                          label= "ingrese nombre:")
    precio = IntegerField(label= "ingrese precio:",
                          validators =[ InputRequired(
                                            message="precio requerido"),
                                        NumberRange(
                                            min= 0,
                                            max =200
                                        )
                                      ])
    imagen = FileField(label="Cargue imagen del producto",
                       validators= [FileRequired(message="se requiere una imagen"),
                                    FileAllowed(
                                        ["jpg" ,"png","jfif", "jpeg"],
                                        message="tipo de archivo incorrecto"
                                    )
                                    ])
    submit = SubmitField("Registro")
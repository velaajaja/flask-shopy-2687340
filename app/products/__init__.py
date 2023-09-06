#dependencia para hacer un blueprint
from flask import Blueprint

#definir paquete 'products'
products = Blueprint('products',__name__,url_prefix='/products',template_folder='templates')
static_folder = 'imagenes'
from . import routes
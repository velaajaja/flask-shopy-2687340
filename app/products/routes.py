from flask import render_template
from . import products
from .forms import NewProductForm
import app
import os

@products.route('/create' , methods=["GET","POST"])
def crear_product():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        #llenar atributos del objeto producto
        form.populate_obj(p)
        #registrar productos en bd
        app.db.session.add(p)
        p.imagen = form.imagen.data.filename
        app.db.session.commit()
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + '/app/products/imagenes/' + p.imagen) )
        #trasladar la imagen cargada
        #a la carpeta app/products/imagenes
        return os.getcwd()
        
    return render_template('new.html', form = form) 
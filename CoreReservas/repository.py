import datetime

from models.producto import *
from models.cliente import *
from models.pedido import *
from models.formato_botella import *
from models.tipo_corcho import *

lista_productos = {
    0: Producto(0,"Vino Tinto","Un vino que es tinto",30.0,FormatoBotella.ESTANDAR,TipoCorcho.NATURAL,datetime.datetime.now()),
    1: Producto(1,"Vino Rosado","Un vino que es rosado",30.0,FormatoBotella.ESTANDAR,TipoCorcho.NATURAL,datetime.datetime.now()),
    2: Producto(2,"Vino Blanco","Un vino que es blanco",30.0,FormatoBotella.ESTANDAR,TipoCorcho.NATURAL,datetime.datetime.now()),
    3: Producto(3,"Vino Blanco","Un vino que es blanco",30.0,FormatoBotella.MEDIA_BOTELLA,TipoCorcho.AGLOMERADO,datetime.datetime.now())
}


next_productos_index = 4

def get_lista_productos():
    global lista_productos
    return lista_productos

def get_next_productos_index():
    global next_productos_index
    return next_productos_index

def add_producto(producto):
    global lista_productos
    global next_productos_index
    lista_productos.update({producto.id:producto})
    next_productos_index += 1

def update_producto(producto):
    global lista_productos
    global next_productos_index
    lista_productos.update({producto.id:producto})

def get_producto_by_id(id):
    global lista_productos
    return lista_productos[id]
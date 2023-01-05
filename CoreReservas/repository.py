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


lista_clientes = {
    0: Cliente(0,"Joselito","Arrojo Abela","77192949G","C/Clara Campoamor","656697741",datetime.datetime.now()),
    1: Cliente(1,"Pepito","Torrojo Unavela","64626177G","C/Timon","655767152",datetime.datetime.now()),
    2: Cliente(2,"Pepito","Torrojo Unavela","77192949G","C/Carla Amor de Campo","656697741",datetime.datetime.now()),
    3: Cliente(3,"Joselito","Arrojo Abela","64626177G","P/ Malagueta","655767151",datetime.datetime.now()),
}

next_clientes_index = 4

# Clientes

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

# Clientes

def get_lista_clientes():
    global lista_clientes
    return lista_clientes

def get_next_clientes_index():
    global next_clientes_index
    return next_clientes_index

def add_cliente(cliente):
    global lista_clientes
    global next_clientes_index
    lista_clientes.update({cliente.id:cliente})
    next_clientes_index += 1

def update_cliente(cliente):
    global lista_clientes
    global next_clientes_index
    lista_clientes.update({cliente.id:cliente})

def get_cliente_by_id(id):
    global lista_clientes
    return lista_clientes[id]
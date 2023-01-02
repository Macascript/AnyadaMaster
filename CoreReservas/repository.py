import datetime

from models.producto import *
from models.cliente import *
from models.pedido import *
from models.formato_botella import *
from models.tipo_corcho import *

lista_productos = [
    Producto(0,"Vino Tinto","Un vino que es tinto",30.0,FormatoBotella.ESTANDAR,TipoCorcho.NATURAL,datetime.datetime.now()),
    Producto(0,"Vino Rosado","Un vino que es rosado",30.0,FormatoBotella.ESTANDAR,TipoCorcho.NATURAL,datetime.datetime.now()),
    Producto(0,"Vino Blanco","Un vino que es blanco",30.0,FormatoBotella.ESTANDAR,TipoCorcho.NATURAL,datetime.datetime.now()),
    Producto(0,"Vino Blanco","Un vino que es blanco",30.0,FormatoBotella.MEDIA_BOTELLA,TipoCorcho.AGLOMERADO,datetime.datetime.now())
]

def get_lista_productos():
    global lista_productos
    return lista_productos

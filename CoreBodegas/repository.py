import datetime

from models.materia_prima import *
from models.personal import *

lista_materias_primas = {
    0: MateriaPrima(0,
        "Cabernet Sauvignon",
        "Mu rica",
        310,
        50.0,
        TipoUva.ROJAS,
        datetime.datetime.now(),
        1,
        1
    ),
    1: MateriaPrima(1,
        "Garnacha",
        "Solo rica",
        510,
        50.0,
        TipoUva.ROJAS,
        datetime.datetime.now(),
        2,
        2
    ),
    2: MateriaPrima(2,
        "Graciano",
        "No tan rica",
        110,
        50.0,
        TipoUva.ROJAS,
        datetime.datetime.now(),
        3,
        1
    ),
    3: MateriaPrima(3,
        "Monastrell",
        "No está rica y punto",
        10,
        50.0,
        TipoUva.ROJAS,
        datetime.datetime.now(),
        2,
        1
    )
}

next_materias_primas_index = 4
# max_height = 3

lista_personal = {
    0: Personal(0,
        "Perico",
        "Pilatos",
        "2134124124F",
        "A318u81342",
        datetime.datetime.now(),
        "C/ Alpargata",
        "678901234",
        "Pepito: 6123345789",
        CategoriaLaboral.PERSONAL,
        datetime.datetime.now(),
        EstadoCivil.CASADO
    ),
    1: Personal(2,
        "Perico",
        "Pilatos",
        "2134124124F",
        "A318u81342",
        datetime.datetime.now(),
        "C/ Alpargata",
        "678901234",
        "Pepito: 6123345789",
        CategoriaLaboral.PERSONAL,
        datetime.datetime.now(),
        EstadoCivil.CASADO
    ),
    2: Personal(2,
        "Perico",
        "Pilatos",
        "2134124124F",
        "A318u81342",
        datetime.datetime.now(),
        "C/ Alpargata",
        "678901234",
        "Pepito: 6123345789",
        CategoriaLaboral.PERSONAL,
        datetime.datetime.now(),
        EstadoCivil.CASADO
    ),
    3: Personal(3,
        "Perico",
        "Pilatos",
        "2134124124F",
        "A318u81342",
        datetime.datetime.now(),
        "C/ Alpargata",
        "678901234",
        "Pepito: 6123345789",
        CategoriaLaboral.PERSONAL,
        datetime.datetime.now(),
        EstadoCivil.CASADO
    )
}

next_personal_index = 4

# Pedidos

def get_lista_materias_primas():
    global lista_materias_primas
    return lista_materias_primas

def get_next_materias_primas_index():
    global next_materias_primas_index
    return next_materias_primas_index

def add_materia_prima(materia_prima):
    global lista_materias_primas
    global next_materias_primas_index
    lista_materias_primas.update({materia_prima.id:materia_prima})
    next_materias_primas_index += 1

def update_materia_prima(materia_prima):
    global lista_materias_primas
    global next_materias_primas_index
    lista_materias_primas.update({materia_prima.id:materia_prima})

def get_materia_prima_by_id(id):
    global lista_materias_primas
    return lista_materias_primas[id]

# def get_max_height():
#     global max_height
#     return max_height * 20

# Personal

def get_lista_personal():
    global lista_personal
    return lista_personal

def get_next_personal_index():
    global next_personal_index
    return next_personal_index

def add_personal(personal):
    global lista_personal
    global next_personal_index
    lista_personal.update({personal.id:personal})
    next_personal_index += 1

def update_personal(personal):
    global lista_personal
    global next_personal_index
    lista_personal.update({personal.id:personal})

def get_personal_by_id(id):
    global lista_personal
    return lista_personal[id]


historial = [
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito",
    f"[{datetime.datetime.now()}] Personal Perico Pilatos 2134124124F ha eliminado el pedido (0) del cliente (0) Joselito"
]

def get_historial():
    global historial
    return historial
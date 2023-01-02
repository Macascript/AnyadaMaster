from dataclasses import dataclass

from models.producto import Producto

@dataclass
class Item:
    producto: Producto
    cantidad: int

@dataclass
class Pedido:
    id: int
    cantidad: int
    precio: float
    descuento: float
    productos: Item

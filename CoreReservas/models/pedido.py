from dataclasses import dataclass

from models.producto import Producto
from models.cliente import Cliente

@dataclass
class Item:
    producto: Producto
    cantidad: int

@dataclass
class Pedido:
    id: int
    cliente: Cliente
    descuento: float
    items: list

    def items_str(self):
        string = ""
        for item in self.items:
            string += f"({item.producto.id}) {item.producto.nombre} x{item.cantidad}\n"
        return string

    def tolist(self):
        return [
            f"({self.cliente.id}) {self.cliente.nombre} {self.cliente.apellidos}",
            self.descuento,
            self.items_str()
        ]

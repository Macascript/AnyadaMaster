from dataclasses import dataclass
import datetime
from datetime import date

from models.formato_botella import FormatoBotella
from models.tipo_corcho import TipoCorcho

@dataclass
class Producto:
    id: int
    nombre: str
    descripcion: str
    precio: float
    formato_botella: FormatoBotella
    tipo_corcho: TipoCorcho
    cosecha: date

    def tolist(self):
        return [
            self.nombre,
            self.descripcion,
            self.precio,
            f"{self.formato_botella.value} ({self.formato_botella.name})",
            self.tipo_corcho.name,
            self.cosecha.strftime("%m/%Y")
        ]
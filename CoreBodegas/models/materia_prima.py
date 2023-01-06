from dataclasses import dataclass, field
from datetime import date

from models.tipo_uva import TipoUva

@dataclass
class MateriaPrima():
    id: int
    nombre: str
    descripcion: str
    codigo_origen: int
    cantidad: float
    tipo_uva: TipoUva
    fecha: date
    madurez: int
    calidad: int

    def tolist(self):
        return [
            self.nombre,
            self.descripcion,
            self.codigo_origen,
            self.cantidad,
            self.tipo_uva.name,
            self.fecha.strftime("%d/%m/%Y"),
            self.madurez,
            self.calidad
        ]
from dataclasses import dataclass
from datetime import date

@dataclass
class Cliente:
    id: int
    nombre: str
    apellidos: str
    nif: str
    direccion: str
    telefono: str
    fecha_nacimiento: date

    def tolist(self):
        return [
            self.nombre,
            self.apellidos,
            self.nif,
            self.direccion,
            self.telefono,
            self.fecha_nacimiento.strftime("%d/%m/%Y")
        ]
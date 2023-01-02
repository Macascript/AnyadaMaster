from dataclasses import dataclass
import datetime

@dataclass
class Cliente:
    id: int
    nombre: str
    apellido: str
    nif: str
    direccion: str
    telefono: str
    fecha_nacimiento: datetime
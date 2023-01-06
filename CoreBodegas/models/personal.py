from dataclasses import dataclass
from datetime import date

from models.categoria_laboral import CategoriaLaboral
from models.estado_civil import EstadoCivil

@dataclass
class Personal:
    id: int
    nombre: str
    apellidos: str
    nif: str
    seguridad_social: str
    fecha_nacimiento: date
    domicilio: str
    telefono: str
    contacto_emergencia: str
    categoria_laboral: CategoriaLaboral
    fecha_ingreso: date
    estado_civil: EstadoCivil

    def tolist(self):
        return [
            self.nombre,
            self.apellidos,
            self.nif,
            self.seguridad_social,
            self.fecha_nacimiento.strftime("%d/%m/%Y"),
            self.domicilio,
            self.telefono,
            self.contacto_emergencia,
            self.categoria_laboral.name,
            self.fecha_ingreso.strftime("%d/%m/%Y"),
            self.estado_civil.name
        ]
from enum import Enum

class FormatoBotella(Enum):
    MEDIA_BOTELLA = 0.375
    ESTANDAR = 0.75
    MAGNUM = 1.5
    DOBLE_MAGNUM = 3
    JEROBOAM = 4.5
    IMPERIAL = 6
    SALMANAZAR = 9
    BALTASAR = 12
    NABUCODONOSOR = 15

    def tostring(self):
        f"{self.value} ({self.name})"
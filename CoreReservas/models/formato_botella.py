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
    
    @staticmethod
    def tolist():
        return ["MEDIA_BOTELLA","ESTANDAR","MAGNUM","DOBLE_MAGNUM","JEROBOAM","IMPERIAL","SALMANAZAR","BALTASAR","NABUCODONOSOR"]

    @staticmethod
    def strtoenum(s):
        if s == "MEDIA_BOTELLA": return FormatoBotella.MEDIA_BOTELLA
        if s == "ESTANDAR": return FormatoBotella.ESTANDAR
        if s == "MAGNUM": return FormatoBotella.MAGNUM
        if s == "DOBLE_MAGNUM": return FormatoBotella.DOBLE_MAGNUM
        if s == "JEROBOAM": return FormatoBotella.JEROBOAM
        if s == "IMPERIAL": return FormatoBotella.IMPERIAL
        if s == "SALMANAZAR": return FormatoBotella.SALMANAZAR
        if s == "BALTASAR": return FormatoBotella.BALTASAR
        if s == "NABUCODONOSOR": return FormatoBotella.NABUCODONOSOR
        return FormatoBotella.MEDIA_BOTELLA
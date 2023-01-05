from enum import Enum

class TipoCorcho(Enum):
    NATURAL = 0
    COLMATADO = 1
    UNOMASUNO = 2
    AGLOMERADO = 3
    SINTETICO = 4

    @staticmethod
    def tolist():
        return ["NATURAL","COLMATADO","UNOMASUNO","AGLOMERADO","SINTETICO"]
    
    @staticmethod
    def strtoenum(s):
        if s == "NATURAL": return TipoCorcho.NATURAL
        if s == "COLMATADO": return TipoCorcho.COLMATADO
        if s == "UNOMASUNO": return TipoCorcho.UNOMASUNO
        if s == "AGLOMERADO": return TipoCorcho.AGLOMERADO
        if s == "SINTETICO": return TipoCorcho.SINTETICO
        return TipoCorcho.NATURAL
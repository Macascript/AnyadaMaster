from enum import Enum

class TipoUva(Enum):
    ROJAS = 0
    BLANCAS = 1

    @staticmethod
    def tolist():
        return [
            "ROJAS",
            "BLANCAS"
        ]
    
    def strtoenum(s):
        if s == "ROJAS": return TipoUva.ROJAS
        if s == "BLANCAS": return TipoUva.BLANCAS
        return TipoUva.ROJAS
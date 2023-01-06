from enum import Enum

class EstadoCivil(Enum):
    CASADO = 0
    SOLTERO = 1
    SEPARADO = 2
    DIVORCIADO = 3

    @staticmethod
    def tolist():
        return [
            "CASADO",
            "SOLTERO",
            "SEPARADO",
            "DIVORCIADO"
        ]
    
    @staticmethod
    def strtoenum(s):
        if s == "CASADO": return EstadoCivil.CASADO
        if s == "SOLTERO": return EstadoCivil.SOLTERO
        if s == "SEPARADO": return EstadoCivil.SEPARADO
        if s == "DIVORCIADO": return EstadoCivil.DIVORCIADO
        return EstadoCivil.SOLTERO
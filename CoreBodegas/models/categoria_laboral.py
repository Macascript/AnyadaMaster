from enum import Enum

class CategoriaLaboral(Enum):
    PERSONAL = 0
    ADMINISTRATIVO = 1

    @staticmethod
    def tolist():
        return [
            "PERSONAL",
            "ADMINISTRATIVO"
        ]
    
    @staticmethod
    def strtoenum(s):
        if s == "PERSONAL": return CategoriaLaboral.PERSONAL
        if s == "ADMINISTRATIVO": return CategoriaLaboral.ADMINISTRATIVO
        return CategoriaLaboral.PERSONAL
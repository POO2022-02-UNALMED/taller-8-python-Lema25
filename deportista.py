from persona import Persona

class Deportista(Persona):
    def __init__(self,nombre,edad,altura,sexo,deporte,años):
        super().__init__(nombre,edad,altura,sexo)
        self._deporte=deporte
        self._añosPracticando=años   

    def setDeporte(self,nuevo):
        self._deporte=nuevo

    def setAñosPracticando(self,nuevo):
        self._añosPracticando=nuevo

    def getDeporte(self):
        return self._deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando


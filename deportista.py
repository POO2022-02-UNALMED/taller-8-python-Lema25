class Deportista:
    def __init__(self,deporte,años):
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


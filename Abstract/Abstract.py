from abc import ABC, abstractmethod

class Expresion(ABC):
    def __init__(self,fila,columna) -> None:
        self.fila = fila
        self.columna = columna

    @abstractmethod #todo se opera
    def operar(self,arbol):#manejamos arbol
        pass
    
    @abstractmethod   
    def getfila(self):
        return self.fila
    @abstractmethod
    def getcolumna(self):
        return self.columna
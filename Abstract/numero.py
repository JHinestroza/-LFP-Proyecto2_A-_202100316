from Abstract.Abstract import Expresion

class Numero(Expresion): #esta heredadnod de nuestro metodo abstracto
    def __init__(self, valor, fila, columna) -> None:
        self.valor = valor

        super().__init__(fila, columna)
    
    def operar(self, arbol):
        return self.valor
    
    def getfila(self):
        return super().getfila()
    
    def getcolumna(self):
        return super().getcolumna()
    
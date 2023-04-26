from Abstract.Abstract import Expresion

class Lexema(Expresion):
    def __init__(self,lexema,fila,columna) -> None:
        self.lexema = lexema
        super().__init__(fila, columna)
    
    def operar(self,arbol):
        return self.lexema
    
    def getlexema(self):
        return self.lexema
    
    def getfila(self):
        return super().getfila()
    
    def getcolumna(self):
        return super().getcolumna()
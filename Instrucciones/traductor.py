from Abstract.Abstract import Expresion
from math import *
class Arimetica(Expresion):
    def __init__(self, izquierda,derecha, tipo, fila,columna) -> None:
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        leftvalue = ''
        rightvalue = ''
        #verificar que los numeros no vengan vacios
        if self.izquierda != None:
            leftvalue = self.izquierda.operar(arbol)
        if self.derecha != None:
            rightvalue = self.derecha.operar(arbol)
        
        if self.tipo.operar(arbol) == 'CrearBD':
            return 'use(‘nombreBaseDatos’);'
        elif self.tipo.operar(arbol) == 'EliminarBD':
            return 'db.dropDatabase();'
        elif self.tipo.operar(arbol) == 'CrearColeccion':
            return 'db.createCollection(‘nombreColeccion’); '
        elif self.tipo.operar(arbol) == 'EliminarColeccio':
            return 'db.nombreColeccion.drop();'

        
        
    def getfila(self):
        return super().getfila()
    
    def getcolumna(self):
        return super().getcolumna()
    
    def gettipo(self):
        tipo = self.tipo
        
        return tipo
    
    
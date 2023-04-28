from Abstract.Abstract import Expresion
from math import *


class Arimetica(Expresion):
    def __init__(self, funcion,nombre, fila,columna) -> None:
        self.funcion = funcion
        self.nombre = nombre
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        nombre = ''
        if self.nombre != None:
            nombre = self.nombre.operar(arbol)
        
        if self.funcion.operar(arbol) == 'CrearBD()':
            return f'use(‘{nombre}’);'
        elif self.funcion.operar(arbol) == 'EliminarBD()':
            return f'db.dropDatabase(‘{nombre}’);'
        elif self.funcion.operar(arbol) == f'CrearColeccion(“{nombre}”)':
            return f'db.createCollection(‘{nombre}’);'
        elif self.funcion.operar(arbol) == 'EliminarColeccio()':
            return f'db.nombreColeccion.drop(‘{nombre}’);'
        
        
    def getfila(self):
        return super().getfila()
    
    def getcolumna(self):
        return super().getcolumna()
    
    def gettipo(self):
        tipo = self.tipo
        
        return tipo
    
    
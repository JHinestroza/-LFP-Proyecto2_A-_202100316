from Abstract.Abstract import Expresion

class Errores(Expresion):
    def __init__(self, lexema, fila, columna) -> None:
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, no):
        no_ = f'\t\t"No.":{no}\n '
        desc = '\t\t"Descrepcion-token": {\n'
        lex = f'\t\t\t"Lexema":{self.lexema}\n'
        tipo = '\t\t\t"Tipo": Error Lexico\n'
        fila = f'\t\t\t"Fila" :{self.fila}\n'
        columna = f'\t\t\t"Columna": {self.columna}\n'
        fin = '\t\t}\n'

        return '\t{\n'+no + desc + lex + tipo + fila + columna + fin +'\t}'
    
    def getcolumna(self):
        return super().getcolumna()
    
    def getfila(self):
        return super().getfila()

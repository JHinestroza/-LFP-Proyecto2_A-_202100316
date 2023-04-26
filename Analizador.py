from Instrucciones.traductor import *
from Abstract.Lexema import *
from Abstract.numero import *
from Graficar import Grafica
from Errores.errores import *



global n_lineas
global n_columnas
global instrucciones
global lista_lexemas
global lista_errores

n_lineas = 1
n_columnas = 1
lista_lexemas = []
instrucciones = []
lista_errores = []

def instruccion(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    lexema = ''
    puntero = 0 #para reducir la cadena de caracteres

    while cadena:
        char =  cadena[puntero]
        if char == 'ñ':
            continue
    
        elif char == "[" or char == "]":
            n_columnas +=1
            c = Lexema(char,n_lineas,n_columnas)
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0

        elif char == '\t':
            n_columnas +=4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            n_lineas +=1
            n_columnas +=1
            cadena = cadena[1:]
            puntero = 0
        elif char == '=':
            continue
        else:
            lexema,cadena = armar_lexema(cadena[puntero:]) #actualiza la cadena para que no recorra de nuevo todo
            if lexema and cadena:
                n_columnas +=1
                l = Lexema(lexema, n_lineas, n_columnas)
                lista_lexemas.append(l)
                n_columnas += len(lexema)+1
                puntero = 0 # se reinicia porque la cadena viene actualizada
        

def armar_lexema(cadena): #arma el lexeme el cual se utiliza para 
    global n_lineas
    global n_columnas
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '\n':
            return lexema, cadena[len(puntero):] #corta la cedena
        else:
            lexema +=char
    return None, None


def imprimir():
    for lexema in lista_lexemas:
        print(lexema.lexema)

def graficar():
    
    Grafica.Graficar(instrucciones)

def getErrores():
    global lista_errores
    return lista_errores

def getErrores_():
    lista_errores = getErrores()
    contador = 1
    print('{')
    while lista_errores:
        error = lista_errores.pop(0)
        print(error.operar(contador), ",")
        contador +=1
    print('}')

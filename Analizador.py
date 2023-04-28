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
        if puntero < len(cadena) -1:
            puntero +=1
        else:
            break

        if char == '=':
            lexema,cadena = armar_funcion(cadena[puntero:]) #actualiza la cadena para que no recorra de nuevo todo
            if lexema and cadena:
                n_columnas +=1
                l = Lexema(lexema, n_lineas, n_columnas)
                lista_lexemas.append('Funcion')
                lista_lexemas.append(l)
                n_columnas += len(lexema)+1
                puntero = 0 # se reinicia porque la cadena viene actualizada
            
        elif char == "(" or char == ")":
            n_columnas +=1
            c = Lexema(char,n_lineas,n_columnas)
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0

        elif char == '\t':
            n_columnas +=4
            cadena = cadena[4:]
            puntero = 0
        elif char == ' \n':
            n_lineas +=1
            n_columnas +=1
            cadena = cadena[1:]
            puntero = 0
        elif cadena[0]:
            nombre, cadena = armar_nombre(cadena)
            if nombre and cadena :
                n_columnas +=1
                n = Numero(nombre, n_lineas, n_columnas)
                lista_lexemas.append('Nombre')
                lista_lexemas.append(n)
                n_columnas += len(str(nombre))+1
                puntero = 0
        else:
            lista_errores.append(Errores(char,n_lineas,n_columnas))
            cadena = cadena[1:]
            puntero = 0
            n_columnas +=1
            

    # for lexema in lista_lexemas:
        
    #     print(lexema)
        

def armar_funcion(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    lexema = ''
    puntero = ''
    contador = 0
    for char in cadena:
        puntero += char
        if char == ' ':
            nuevo = puntero.replace(" ", "")
        elif char == ';':
            funcion = lexema[len(nuevo):]
            return funcion, cadena[len(puntero):]
        else:
            lexema +=char
    return None, None


def armar_nombre(cadena):
    nombre = ''
    lexema = ''
    puntero = ''
    contador = 0
    for char in cadena:
        puntero += char
        if char == ' ':
            if contador == 0:
                funcion = puntero.replace(" ", "")
                contador +=1

        elif char == '=' : #indica donde termina nuestro numero
            nombre = lexema[len(funcion):]
            return nombre, cadena[len(puntero)-1:]
        else:
            lexema +=char


def operar():
    global lista_lexemas
    global instruccion
    lexema = ''
    funcion= ''

    while lista_lexemas:
        lexema = lista_lexemas.pop(0) #eliminamos un elemento de la lista
        if lexema == 'Nombre':
            nombre = lista_lexemas.pop(0)
        elif lexema == 'Funcion':
            funcion = lista_lexemas.pop(0)
        
        if nombre and funcion:
            return(Arimetica(funcion,nombre,f'Inicio: {funcion.getfila()} : {funcion.getcolumna()}', F'Fin: {nombre.getfila()}: {nombre.getcolumna()}'))
        

def _operar():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else: 
            break
    for instruccion in instrucciones:
        print(instruccion.operar(None))
    return instrucciones


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

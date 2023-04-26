import graphviz
from graphviz import Digraph, Source

class Grafica():
    def Graficar(lista_lexema):
        g= graphviz.Digraph('ejempplo', filename = 'lista pelis')
        g.attr(fontsize='12' , width='0.9')

        
        for lista in lista_lexema:
            print(lista.izquierda.operar(None))
            print(lista.derecha.operar(None))
            print(lista.tipo.operar(None))
            # grafica.node(lista.izquierda.operar(None),lista.izquierda.operar(None))
            # grafica.node(lista.derecha.operar(None), lista.derecha.operar(None))
            # grafica.node(lista.tipo.operar(None), lista.tipo.operar(None),)
            g.node(str(lista.izquierda.operar(None)),str(lista.izquierda.operar(None)), shape='circle')
            g.node(str(lista.derecha.operar(None)),str(lista.derecha.operar(None)) ,shape='circle')
            
            g.node(str(lista.tipo.operar(None)),str(lista.tipo.operar(None)), shape='circle')
            g.edge(str(lista.izquierda.operar(None)), str(lista.tipo.operar(None)) )
            g.edge(str(lista.derecha.operar(None)), str(lista.tipo.operar(None)))
            # Agregar aristas
            
        g.view()
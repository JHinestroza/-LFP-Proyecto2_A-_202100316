from Analizador import *
import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from Analizador import instruccion,graficar,getErrores_,_operar

class kinter():
    def __init__(self) -> None:
        self.raiz = Tk()
        self.archivo = None
        self.texto = None
        self.bandera = True
        self.text_content = None
        self.doc = None
        self.label = None

    def menu(self):
        #Ventana principal
        self.raiz.title("Proyecto 1")
        self.raiz.geometry("600x650")
        self.raiz.resizable(False,False)
    
        self.frame = Frame(self.raiz)
        self.frame.place(x=0, y=0, width=600, height=650)
        self.frame.config(bg="#30f6ca")

        self.texto = Text (self.frame, wrap=tk.WORD)
        self.texto.place (x=50, y=50,width=450, height=575 )

        self.texto.bind('<KeyRelease>', self.actualizar_posicion)

        self.label = tk.Label(self.frame, text="Fila: 1, Columna: 0")
        self.label.place(x=50, y=600,width=150, height=25)

        self.b1 = Button(self.frame,command=self.Archivo, text="Archivo",bg="#ADD8E6").place(x=0, y= 0, width=150, height=30)
        self.b4 = Button(self.frame, text="Analizar",command= self.analizar, bg="#ADD8E6").place(x=150, y= 0, width=150, height=30)
        self.b6 = Button(self.frame, text="Salir", command=self.raiz.destroy, bg="#ADD8E6").place(x=300, y= 0, width=150, height=30)
        self.raiz.mainloop() #mantiene la aplicacion grafica abierta
    
    def Editararchivo(self):
        self.archivo = filedialog.askopenfilename(title="operaciones",initialdir="C:/Users/Hinestroza/Desktop/Proyectos Lenguajes",
                    filetypes=[("Archivo txt", "*.txt")])
        archivo = open(self.archivo,"r")       
        self.text_content = archivo.read()
        self.eliminartexto()
        self.texto.insert(tk.END,self.text_content)
        self.bandera = False
        #print(self.archivo)

    def Archivo(self):
        self.raiz.geometry("550x675")
        self.frame = Frame(self.raiz)   
        self.frame.place(x=0, y=0, width=550, height=675)

        self.b5 = Button(self.frame, text="Errores",bg="#ADD8E6").place(x=0, y= 0, width=150, height=30)
        
        self.frame.config(bg="#30f6ca")

        self.texto = Text (self.frame, wrap=tk.WORD)
        self.texto.place (x=50, y=50,width=450, height=575 )

        self.texto.bind('<KeyRelease>', self.actualizar_posicion)

        self.label = tk.Label(self.frame, text="Fila: 1, Columna: 0")
        self.label.place(x=50, y=625,width=150, height=25)
        
        self.b1 = Button(self.frame,command=self.eliminartexto, text="Nuevo",bg="#ADD8E6").place(x=0, y= 0, width=50, height=30)
        self.b2 = Button(self.frame,command=self.Editararchivo, text="Abrir",bg="#ADD8E6").place(x=50, y= 0, width=50, height=30)
        self.b3 = Button(self.frame,command=self.guardar, text="Guardar", bg="#ADD8E6").place(x=100, y= 0, width=75, height=30)
        self.b4 = Button(self.frame,command=self.guardar_como, text="Guardar Como",bg="#ADD8E6").place(x=175, y= 0, width=100, height=30)
        self.b5 = Button(self.frame, text="Analizar",command= self.analizar, bg="#ADD8E6").place(x=275, y= 0, width=50, height=30)
        self.b6 = Button(self.frame, text="Salir", command=self.raiz.destroy, bg="#ADD8E6").place(x=325, y= 0, width=150, height=30)

        self.raiz.mainloop()

    def guardar(self):
        if self.bandera:
            messagebox.showinfo("INFO", "No hay archivo cargado")
        else:
            contenido = self.texto.get('1.0', tk.END)
            with open(self.archivo, 'w') as archivo:
                archivo.write(contenido)
        
    def eliminartexto(self):
        self.texto.delete('1.0', tk.END)

    def guardar_como(self):
        contenido = self.texto.get('1.0', tk.END)
        ruta_archivo = filedialog.asksaveasfilename(defaultextension='.txt',
                                                filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if ruta_archivo:
            with open(ruta_archivo, 'w') as archivo:
                archivo.write(contenido)
    
    def analizar(self):
        contenido = self.texto.get('1.0', tk.END)
        instruccion(contenido)
        _operar()

    def actualizar_posicion(self,event):
        posicion = self.texto.index(tk.INSERT)
        fila, columna = posicion.split('.')
        self.label.config(text=f"Fila: {fila}, Columna: {columna}")

ventana = kinter()
ventana.menu()
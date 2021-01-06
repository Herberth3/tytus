#libreria importada para la creacion de ventanas en nuestro escritorio
#import tkinter
from tkinter import *
import tkinter
from c3d import analizarLex, analizarSin,tab_string
from bnf import analizarBNFLex, analizarBNFSin

# creamos una nueva ventana
ventana = Tk()
# funcion para darle tamaño a la ventana
ventana.geometry("900x600")
ventana.configure(bg = "gray")

consola = []

# creamos una etiqueta para mostrar
etiqueta = Label(ventana, text = "SQL PARSER", bg = "green")
etiqueta.config(width=150)
etiqueta.config(font=("Consolas", 28))
# metodo para mostrar la etiqueta
etiqueta.pack(fill = X)

# creamos una etiqueta para mostrar
etiqueta2 = Label(ventana, text = "SALIDA", bg = "gray")
# metodo para mostrar la etiqueta
etiqueta2.place(x = 100 , y = 350)
#etiqueta2.pack(fill = X)

# ======================================================================
#                         METODOS BOTONES
# ======================================================================
# Metodo de analisis de gramatica
def analizar_texto():
    response= txt_consultas.get("1.0","end")
    salida_lexico_ast = analizarLex(response)
    analizarSin(response)
    print(tab_string())

# Metodo para limpiar la salida de gramatica
def limpiar():
    print("limpiando")
    txt_consultas.delete("1.0","end")

# Metodo reporte AST
def reporte():
    print("REPORTE AST")
    response = txt_consultas.get("1.0","end")

# Metodo reporte BNF
def reporteBNF():
    print("REPORTE BNF")
    result= txt_consultas.get("1.0","end")
    salida_Lexico = analizarBNFLex(result)  # se envia el texto a el analizador lexico
    analizarBNFSin(result)  # se envia el texto a el analizador sintactico
    print(salida_Lexico)
    
# ======================================================================
#                               BOTONES
# ======================================================================
#creamos un boton para mostrar
#commad = funcion()
#imagen para el boton
# boton para ejecutar la consulta
imgBoton = PhotoImage(file="imagenes/run.png")
imgBoton = imgBoton.zoom(1)
botonConsulta = Button(ventana,image = imgBoton,padx = 5,pady=5, border = 0,command = analizar_texto)
botonConsulta.config(bg = "gray")
botonConsulta.place(x= 12,y = 60)

#creamos un boton para mostrar
#imagen para el boton
#boton para limpiar la pantalla
imgBoton2 = PhotoImage(file="imagenes/clean.png")
imgBoton2 = imgBoton2.zoom(1)
botonLimpiar = Button(ventana,image = imgBoton2,padx = 5,pady=5, border = 0,command = limpiar)
botonLimpiar.config(bg = "gray")
botonLimpiar.place(x= 12,y = 145)

#creamos un boton para reporte AST
#imagen para el boton
imgBoton3 = PhotoImage(file="imagenes/ast.png")
imgBoton3 = imgBoton3.zoom(1)
botonLimpiar = Button(ventana,image = imgBoton3,padx = 5,pady=5, border = 0,command = reporte)
botonLimpiar.config(bg = "gray")
botonLimpiar.place(x= 12,y = 230)

#creamos un boton para reporte AST
#imagen para el boton
imgBoton4 = PhotoImage(file="imagenes/bnf.png")
imgBoton4 = imgBoton4.zoom(1)
botonLimpiar = Button(ventana,image = imgBoton4,padx = 5,pady=5, border = 0,command = reporteBNF)
botonLimpiar.config(bg = "gray")
botonLimpiar.place(x= 12,y = 315)

# ======================================================================
#                           TEXTAREA
# ======================================================================
# TEXTAREA Entrada
txt_consultas = Text(ventana,height = 20,width = 130,bg = "black",fg = "white")
txt_consultas.place(x = 100 , y = 60)

# TEXTAREA Salida
txt_salida = Text(ventana,height = 15,width = 130,bg = "black",fg = "green")
txt_salida.place(x = 100 , y = 380)
scrollb = tkinter.Scrollbar( command=txt_salida.yview)
txt_salida['yscrollcommand'] = scrollb.set


# loop para mostrar nuestra venatana
ventana.mainloop()

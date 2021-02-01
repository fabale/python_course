# -*- coding: utf-8 -*-

from tkinter import * # Se importa la librería Tkinter

raiz = Tk()           # Se debe seguir con este código en el mismo orden

raiz.title("Ventana de Pruebas")

# raiz.resizable(True, False)

# raiz.iconbitmap("logo-junior-fc.ico")

# raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame = Frame() # Desde aquí se empieza a crear código para el frame , debajo de la raíz, que es el código principal

miFrame.pack() 

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

raiz.mainloop() # Siempre debe ir de último

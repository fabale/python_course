# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()


varOpcion = IntVar()

Label(root)

Radiobutton(root, text = "Masculino", variable = varOpcion, value = 1).pack()

Radiobutton(root, text = "Femenino", variable = varOpcion, value = 2).pack()





root.mainloop()


from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=600)

miFrame.pack()

miImagen=PhotoImage(file="tenor.gif")

Label(miFrame, image=miImagen).place(x=200, y=200)


root.mainloop()

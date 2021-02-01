from tkinter import *
from tkinter import scrolledtext # Módulo que nos permite hacer que aparezca el Scroll automáticamente
 
raiz=Tk() #Código que define la raiz de la aplicación y no debe faltar. raiz es la variable que puede ser otra
		  # y Tk es fijo, es el llamado de la librería tkinter.

miFrame=Frame(raiz, width=1200, height=600)  # miFrame es la variable que puede ser de otro nombre y define las medidas
											 # del cuadro. raiz es para identificar que miFrame está dentro suyo y
											 # es hijo.
miFrame.pack()		# pack empaqueta la variable miFrame para que solo ocupe el espacio de los elementos.

# cuadroTexto=Entry(miFrame) # cuadroTexto es el nombre de la variable y Entry es el método (es un cuadro de texto) y
						  # miFrame representa el lugar al que pertenece dicha variable, y que es hijo de raiz.

# cuadroTexto.grid(row=0, column=0) # El método grid ayuda a formar una grilla, como en Front-End y row y column
								  # determinan la dimensión; ambas inician desde 0 (cero).

# nombreLabel=Label(miFrame, text="Nombre:") # nombreLabel es la variable que uiliza el método Label para escribir texto
										   # en el cuadro y miFrame indica que pertenece a esa variable, que a su vez
										   # pertenece a raiz.							  

# nombreLabel.place(x=120, y=100)			   # place es un método que nos permite registrar las cordenadas donde vamos
										   # a ubicar el Label: x es la medida horizontal y y la vertical, como en
										   # plano cartesiano.

minombre=StringVar() # La variable minombre de la línea 78 es relacionada con esta que debe almacenar cadena de
					 # caracteres, cmo así lo indica StringVar.

cuadroNombre=Entry(miFrame, textvariable=minombre) # textvariable sirve para almacenar en cuadroNombre la variable minombre
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)

cuadroUser=Entry(miFrame)
cuadroUser.grid(row=3, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=4, column=1, padx=10, pady=10)
cuadroPass.config(show="*")     # El método config nos permite configurar o personalizar el texto ingresado en Entry

cuadroTexto=Text(miFrame, width=19, height=5)
cuadroTexto.grid(row=5, column=1, padx=10, pady=10)

scrollVert=scrolledtext.ScrolledText(miFrame, width=18, height=5)
scrollVert.grid(row=5, column=1, padx=10, pady=10, sticky="nse") # Sticky nos permite dar direción al elemento. n = north. s = south
												# e = east. w = west.

# cuadroTexto.config(yscrollcommand=scrollVert.set) # Con este código configuramos el posicionador o barra de desplazamiento.


nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

userLabel=Label(miFrame, text="Usuario:")
userLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña:")
passLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#######################
# Botones
#######################

def codigoBoton(): #Definimos esta función para crear una orden al presionar el botón Enviar.

	minombre.set("Uno") # minombre es la variable y set le asigna a esa variable lo que está adentro como paŕametro.

botonEnviar=Button(raiz, text="Enviar", command=codigoBoton) # El botón no lo ubicamos en miFrame, sino en el contenedor padre, o sea, raiz.
															 # command lo utilizamos para dar una orden al presionar el botón
botonEnviar.pack()


raiz.mainloop()
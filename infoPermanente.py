# -*- coding: utf-8 -*-

import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona nueva con el nombre de", self.nombre)

	def __str__(self):
		return "{}, {}, {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]         # En esta lista se irán almacenando las personas que se creen en la variable p.

	def __init__(self): # Se crea este constructor para que haga las tareas de crear lista y guardar la
						# información en el archivo externo.

		listaDePersonas = open("archivoExterno", "ab+") # En ficheroExterno almacenamos los datos de personas
														# con el método append para agregar binarios
		listaDePersonas.seek(0)	# Esto sirve para que el cursor se desplace a la posición 0 después de haberse
								# agregado la información en el archivoExterno para leerla desde el inicio.
								
		try:					# Se crea una excepción para cuando no se haya cargado ningún dato y no muestre error
			self.personas = pickle.load(listaDePersonas) # Con esto se busca cargar (volcar) la información en la lista
														 # personas
			print("Se cargaron {} personas del fichero externo".format(len(self.personas))) # Muestra la cantidad
																				 			   # de personas guardadas
																							   # en la lista personas													 																				
		except:
			print("El archivo está vacío")

		finally:				# Con esto se busca cerrar y eliminar lo almacenado temporalmente en memoria
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnArchivoExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnArchivoExterno(self):
		listaDePersonas = open("archivoExterno", "wb")
		pickle.dump(self.personas, listaDePersonas) # Se vuelca la información de listaDePersonas a personas
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoArchivoExterno(self): # Se muestra toda la información creada en archivoExterno
		print("La información del archivo externo es la siguiente:")
		for p in self.personas:
			print(p)

miLista=ListaPersonas() # Se crea el objeto miLista para instanciar (llamar) la clase ListaPersonas.

persona = Persona("Antonio", "Masculino", 42)

miLista.agregarPersonas(persona)
miLista.mostrarInfoArchivoExterno()



		
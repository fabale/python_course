import pickle

class Vehiculos():

	def __init__(self, marca, modelo): #Constructor de la clase padre Vehiculos

		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, 
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

# Creamos los siguientes objetos y serializarlos en una colección de objetos:

carro1 = Vehiculos("Mazda", "MX5")

carro2 = Vehiculos("Seat", "Leon")

carro3 = Vehiculos("Renault", "Megane")

carros = [carro1, carro2, carro3] # Esta es una colección de objetos de tipo carros

fichero = open("losCarros", "wb") # losCarros es el nombre que se le da a los archivos serializados, o sea, 
								  # a lo que guardará la variable fichero.
								  # fichero es un objeto externo que guarda la información serializada en memoria
								  # y los permisos wb (esritura de bytes).

pickle.dump(carros, fichero) # Para hacer el volcado (guardar) de información se crean estas líneas.
							 # fichero es el nombre del archivo donde tenemos los objetos (origen)

fichero.close()				 # Cerramos el fichero.

del (fichero)		 		 # Eliminamos el fichero de la memoria.

ficheroApertura = open("losCarros", "rb")# Con la variable ficeheroApertura se abre (se lee) el archivo losCarros

misCarros = pickle.load(ficheroApertura) # La variable misCarros guardará (volcará)la información de ficheroApertura
										 
ficheroApertura.close()					 # Cerramos la variable ficheroApertura ya que su contenido se
										 # guarda en la variable misCarros.

for c in misCarros:
	
	print(c.estado())										  
	



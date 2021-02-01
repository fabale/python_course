class Carro():		   # Clase con su nombre
    largoChasis = 250  # Propiedades o Atributos y sus medidas en centímetros
    anchoChasis = 120  # Tiene 4 propiedades
    ruedas = 4
    enMarcha = False

    def arrancar(self): # Método llamado "arrancar" está siendo definido.
        self.enMarcha = True

    def estado(self):   # Definimos otro Método llamado estado
    	if(self.enMarcha):
    		return "El carro está en marcha"

    	else:
    		return "El carro está detenido" 

miCarro = Carro()       # Se crea el Objeto miCarro y se instancia una clase, o sea, se relaciona o "se llama"
						# la clase Carro. También se le llama Instancia

print("El largo del carro es: ", miCarro.largoChasis)
print("El carro tiene", miCarro.ruedas , "ruedas")

miCarro.arrancar()  # Aquí se está llamando al Método arrancar mediante el Objeto miCarro
					# y a su vez miCarro pasa a ser el argumento o parámetro de arrancar,
					# o sea, se ubica donde está el término self. En otras palabras, 
					# quedaría de la siguiente forma: miCarro.enMarcha = True


print(miCarro.estado())
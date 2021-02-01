class Carro():	        # Clase con su nombre

    def __init__(self): # Esto es un Constructor y nos sirve para dar valor inicial a las propiedades o atributos
        
        self.__largoChasis = 250  # Propiedades o Atributos y sus medidas en centímetros
        self.__anchoChasis = 120  # Tiene 4 propiedades o variables de clases
        self.__ruedas = 4         # Se hace la Encapsulación con los dos guiones bajos (__) para que las propiedades 
        self.__enMarcha = False   # solo se puedan modificar desde dentro de la clase y no desde afuera.


        #*************** M é t o d o s ***************#

    def arrancar(self, arrancamos): # Método llamado "arrancar" está siendo definido. Se incluye el argumento arrancamos.
        self.__enMarcha = arrancamos

        if (self.__enMarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enMarcha and chequeo): # Se necesitan los dos verdaderos para ser True.
            return "El carro está en marcha"

        elif (self.__enMarcha and chequeo == False):
            return "Algo está mal en el chequeo y el carro no puede arrancar" # Si esta opción se da como False, se ejecuta el                                                                    
                                                                     # código del Else siguiente, por defecto.
        else:

            return "El carro está detenido"


    def estado(self):   # Definimos otro Método llamado estado
    	print("El carro tiene" , self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def __chequeo_interno(self): # Con los dos guiones bajos (__) estamos encapsulando el Método, pues se puede hacer
        print("Realizando chequeo interno")

        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if (self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
            
            return True # El resultado de esto se almacena en el Método chequeo_interno y a su vez en la línea 17. 

        else:

            return False

            # *************** Zona de llamadas ****************** #


miCarro = Carro()       # Se crea el Objeto miCarro y se instancia una clase, o sea, se relaciona o "se llama"
						# la clase Carro
        
print(miCarro.arrancar(True)) # Éste resultado va a la línea 16 y de ser True, llama al método chequeo_interno
                              # (que imprime el mensaje de la línea 34) y su resultado se almacena en la variable chequeo 
miCarro.estado()

print("-------------------------------------------------A continuación creamos el segundo objeto-------------------------------------------------")

otroCarro = Carro()

print(otroCarro.arrancar(False))

otroCarro.estado()
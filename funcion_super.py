class Persona():
	
	def __init__(self, nombre, edad, lugar_residencia): # Método Constructor def __init__
		self.nombre = nombre
		self.edad = edad
		self.lugar_residencia = lugar_residencia

	def descripcion(self):

		print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nLugar de residencia:", self.lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #La función Super llama al método Constructor de la Clase Padre (que es Persona, en este caso),
												  # o sea, al método __init__
												  # Las 3 variables dentro de la función Super se asocian con los 3 argumentos
												  # del método Constructor, a pesar de que tienen nombres diferentes.

		self.salario = salario

		self.antigüedad = antigüedad

	def descripcion(self):

		super().descripcion() 

		print("Salario:", self.salario, "\nAntigüedad:", self.antigüedad)


Manuel = Empleado(1500, 15, "Manuel", 55, "Colombia") # En este caso, Manuel es el nombre de la instancia (Objeto), que puede ser cualquiera
Manuel.descripcion() # Al llamar al método descripción, lo hacemos al de la línea 25 y mediante la función Super de la línea 27
					 # llamamos al método descipción de la Clase Padre de la línea 8; con eso conseguimos ejecutar las 3 variables
					 # de la línea 10 y después las 2 variables restantes de la línea 29.

		

		


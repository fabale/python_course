
"""
for i in [1, 2, 3]:
	print("Hola")

####################################

for estaciones_ano in ["Primavera", "Verano", "Otoño", "Invierno"]:
	print(estaciones_ano)



####################################

for i in ["Píldoras", "Informáticas", 3]: # Para este ejemplo, imprime Hola la cantidad de elementos del bucle for
	print("Hola", end="")				  # o sea, 3 veces.
										  # Con la instrucciń end, se busca que no haya salto de línea para la siguiente
										  # palabra. Si se le da espacio entre comillas, ese será el espacio que habrá
										  # entre palabras. Se debe imprimir 3 veces la palabra Hola.

"""

####################################


email=False

for i in "correo@pildorasinformaticas.es":

	if(i == "@"):

		email = True

if email == True:
	print("El email es correcto")

else:
	print("El email no es correcto")
										  

										
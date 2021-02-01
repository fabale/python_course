# -*- coding: utf-8 -*-


# Ejemplo con una función
"""
def generaPares(limite):

	num=1

	miLista=[]
		
	while num<limite:
		miLista.append(num*2)

		num=num+1

	return miLista

print(generaPares(10))
"""

#############################################################

#Ejemplo con un generador
"""
def generaPares(limite):

	num=1

	while num<limite:
		
		yield num*2

		num=num+1

devuelvePares=generaPares(10)

for i in devuelvePares:
	print(i)
	"""

#############################################################

"""
# Ejemplo con un generador iterando la función
def generaPares(limite):

	num=1

	while num<limite:
		
		yield num*2

		num=num+1

devuelvePares=generaPares(10)

print("Se inicia el código en: " , next(devuelvePares))

print("Seguimos con el código: " , next(devuelvePares))

print("Y así sucesivamente...: " , next(devuelvePares))
"""

#############################################################


def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento: #Esto lo hacemos con el yield en la línea siguiente, por lo que se omite
		yield from elemento


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))












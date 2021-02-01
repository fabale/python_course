# -*- coding: utf-8 -*-

import random
"""
milista=["María", "Pepe", "Marta", "Antonio"]

milista.insert(2,"Sandra")

 print(milista) 


#############################################################################



miTupla=("María", "Pepe", "Marta", "Antonio", 7, False, 10.0)

print (miTupla.index(10.0))


############################################################################# Condicional if
print("Notas de alumnos")
nota_alumno=int(input())

def evaluacion(nota):
	valoracion="Aprobado"
	if nota<5:
		valoracion="Suspenso"
		return valoracion

print(evaluacion(nota_alumno))
"""

############################################################################# Condicional if - else
"""

print("Verificación de acceso")

edad_usuario=int(input("Ingresa tu edad, por favor: "))
if edad_usuario<18:
	print("No puedes pasar")

else:
	print("Puedes pasar")
print("Fin del programa")
"""

#############################################################################
"""

import random

regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']
           
for sorteo in range(5):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)
"""

#############################################################################
"""
print('\nValores posibles: 3, 6, 9, 12, 15')
for i in range(25):
    print(random.randrange(3, 16, 3), end=' ')
"""

#############################################################################
"""

print('\nValores posibles: 0, 1, 2, 3')
for i in range(25):
    print(random.randrange(4), end=' ')

"""
#############################################################################
"""
for numero in range(3):
    print(random.random(), end=' ')
"""


#############################################################################

"""
def run():
  found= 0
  letra=chr(random.randrange(97, 123))  # En ASCII 97:a y 122:z

  while not found:
    letter=input('Escriba una letra: ')

    if letter == letra:
      print('¡¡¡Adivinaste la letra!!!')
      found = 1
    elif ord(letter)>ord(letra):
      print('Está antes en el alfabeto')
    else:
      print('Está después en el alfabeto')

run()
"""

#############################################################################


"""
i=1

while i <=10:
	print("Ejecución " + str(i))
	i=i+1
print("Terminó la ejecución")
"""

#############################################################################





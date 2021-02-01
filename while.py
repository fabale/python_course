# -*- coding: utf-8 -*-

import random
import math

#############################################################################

"""
edad=int(input("Ingrese su edad: "))

while edad<0:
	print("Has ingresado una edad errónea. Inténtalo nuevamente")
	edad=int(input("Ingrese su edad: "))

print("La edad del aspirante es: " + str(edad))
print("Gracias por colaborar. Puedes seguir.")
"""

#############################################################################

print("Calcular raíz cuadrada")
numero=int(input("Ingresa un número: "))

intentos=0

while numero<0:
	print("No se puede hallar raíz cuadrada a un número negativo")
		

	numero=int(input("Ingresa un número: "))
	if numero<0:
		intentos=intentos+1

	if intentos==2:
		print("Has llegado al límite de intentos permitidos. El programa ha finalizado.")
		break

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))
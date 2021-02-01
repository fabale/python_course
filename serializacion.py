# -*- coding: utf-8 -*-

import pickle

# Se escribirá el archivo binario.

"""
lista_nombres = ["Pedro", "Ana", "María", "Isabel"]

archivo_binario = open("lista_nombres", "wb") # Se utiliza el método open y los argumentos son la variable
											  # y wb (w de write y b de binary, porque se exportará el fichero
											  # en binario), o sea, escribir en binario.

pickle.dump(lista_nombres, archivo_binario)	  # Se utiliza la biblioteca pickle que fue importada y el método
											  # dump, que sirve para exportar el archivo binario.
											  # El primer argumento es el del archivo a volcar (o exportar)
											  # y el segundo argumento es el del archivo al que se exportará,
											  # que es un archivo en memoria, que se cerrará.
archivo_binario.close()	# Cerramos el archivo en memoria.										  

del(archivo_binario)    # Eliminamos de la memoria el archivo.
"""

# Se leerá el archivo binario.


archivo = open("lista_nombres", "rb")   # Se escibe el método open y los argumentos son el nombre de archivo
										# a abrir y rb que es read binary, o sea, leer binario al español.

lista = pickle.load(archivo) # Con la biblioteca pickle ya importada se usa el método load para cargar el 
							 # archivo binario. El argumento es el nombre del archivo a cargar o leer, en este caso.

print(lista) # Con esta línea de código se imprime el resultado de la línea anterior, o sea, el contenido
			 # de lista, que se guardó en la variable del mismo nombre y que contiene lo cargado en la línea
			 # 27.
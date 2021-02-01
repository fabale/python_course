# -*- coding: utf-8 -*-

from io import open

"""
archivo_texto = open("archivo.txt", "w") # archivo_texto es la variable. open es el método y los argumentos
										 # archivo.txt es el nombre del archivo y la letra w es de write,
										 # o sea, escribir en español, lo que hace que escriba un texto
										 # en dicho archivo.txt. 
										 
frase = "Estupendo día para estudiar Python \n el miércoles" # frase es la variable y su valor es lo que se
															 # escribe en el archivo.txt


archivo_texto.write(frase) # El método write escribe lo que está entre paréntesis, o sea, la variable frase.

archivo_texto.close() # El método close cierra el archivo que se abrió en memoria en su momento con el método open
					  # en la línea 6.



########################################################



archivo_texto = open("archivo.txt", "r") # En este caso, se cambia el segundo argumento por la letra r de read,
										 # o sea, leer en español, lo que se ecribió en el archivo.txt

texto = archivo_texto.read()	# texto es la variable donde se almacena el resultado de leer el contenido de la 
								# variable archivo_texto.
								# read es el método que nos permitirá leer lo almacenado en archivo_texto.										

archivo_texto.close()			# Con el método close cerramos el archivo creado en archivo_texto

print(texto)					# Con esto se busca imprimir el contenido de texto que, a pesar de haberse cerrado
								# en la la línea anterior, queda almacenado en dicha variable.


# Si se quiere que lo escrito en el archivo.txt se muestre en lista se puede de la siguiente forma:
# lineas_texto = archivo_texto.readlines(), en donde lineas_texto es la variable donde se almacenará 
# el resultado en forma de lista del contenido de archivo_texto y readlines es el método que transforma
# en listas la información del archivo txt.
							


########################################################

archivo_texto = open("archivo.txt", "a") # Para este caso, se cambia el segundo argumento por la letra a
										 # de append, o sea, agregar o añadir en español, para añadirle más 
										 # información a la existente al archivo.txt, que se hizo en la línea 6.

archivo_texto.write("\n Siempre es una buena ocasión para estudiar Python") # Con el método write escribimos
																			# lo que está entre paréntesis
																			# que se añade a lo antes escrito
																			# en el archivo.txt



########################################################

archivo_texto = open("/home/sui_generis/Escritorio/Power BI  - Course", "r")

# print(len(archivo_texto.read())) # Con este código contamos los caracteres del archivo guardado en la variable
								   # archivo_texto.

archivo_texto.seek(len(archivo_texto.read()))								    

print(archivo_texto.read())

"""								   
								 
########################################################

						 
archivo_texto = open("archivo.txt", "r+") # El (segundo) argumento r+ indica que se puede leer (por la letra r)
										  # y escribir (por el símbolo +)
										  
lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta línea ha sido incluída desde el exterior \n"

archivo_texto.seek(0) # Ubica el cursor en la primera posición del archivo con
					  #	el método seek y entre paréntesis la ubicación.

archivo_texto.writelines(lista_texto) #Con writelines se escriben en listas y se guarda en lista_texto

archivo_texto.close() # Cerramos el archivo_texto.





										  
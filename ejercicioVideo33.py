email = input("Ingresa dirección de correo electrónico:")

arroba = email.count('@')

if (arroba!=1 or email.rfind('@') == (len(email)-1) or email.find('@') == 0):
	print("Correo electrónico incorrecto")

else:
	print("Correo electrónico correcto")
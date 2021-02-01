# -*- coding: utf-8 -*-

class Carro():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
        
"""
miVehiculo = Moto()

miVehiculo.desplazamiento()

# Nuevo ejemplo de Polimorfismo creando un objeto otroVehiculo asociándolo al método
# desplazamiento de la clase Carrodatetime A combination of a date and a time. Attributes: ()

otroVehiculo = Carro()

otroVehiculo.desplazamiento()
"""

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo = Moto()

desplazamientoVehiculo(miVehiculo)
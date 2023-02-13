from Animal_py import animal #Itamar
from Vehicle import vehicle  #Itamar
from School import school    #Itamar

"""Creacion de objetos y modificacion de sus atributos usando POO"""

    #instancia clase animal
tigre = animal('tigre','20kg','50cm','40Km/H','Tanzania','Amarillo y negro')
gato = animal('Gato','3kg','16cm','10Km/h','España','blanco')
    #instancia clase vehicle
coche = vehicle('Lamborgini','G200','Italiano','320km/h','Deportivo','Rojo')
coche2= vehicle('Land Rover','XZR2','USA','230Km/h','Todo terreno','Negro')

    #instancias de la clase School
Jaume = school('Jaume Balmes','Barcelona','Programación','1975','26','1192')
Quarto = school('Quarto de Portmany','Ibiza','Ninguna','1987','20','900')


tigre.setVelocidad('80Km/h')
coche.setColor('blanco')
Jaume.setNumPro('40')

tigre.salutacio()
coche.dadesVehicle()
Jaume.datosColegio()


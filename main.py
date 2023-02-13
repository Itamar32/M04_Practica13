from Animal_py import animal #Itamar
from Vehicle import vehicle  #Itamar
from School import school    #Itamar
from book import book #ivan
from user import  user #ivan
from university import university #ivan
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

# A partir de aquí los objetos y sus modificaciones del ejercicio de Iván
#Instancia clase book
Quijote = book("Don Quijote" ,"Blanda","1754","Cervantes","Casablanca","2000")
Lazarillo = book("Lazarillo de tormes","Dura","1800","anonimo","planeta","678")
#Instancia clase user
Ivan = user("Ivan","Montero","Fernández","25","184","Python")
Itamar= user("Itamar","Keydar","Antoni","33","174","Java")
#Instancia clase university
Derecho = university("A","Derecho romano","primero","10","Sí","No")
Matemáticas = university("B","Matemáticas avanzadas","segundo","3","No","Sí")

Quijote.setAutor("Itamar")
Ivan.setEdad("38")
Derecho.setNota("6")

Quijote.nom()
Ivan.salutacio()
Derecho.info()

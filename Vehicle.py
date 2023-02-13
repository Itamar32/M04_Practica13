class vehicle:
    def __init__(self,nombre,modelo,pais,velocidad,tipo,color):
        self.nombre= nombre
        self.modelo= modelo
        self.pais = pais
        self.velocidad =velocidad
        self.tipo= tipo
        self.color= color
    def dadesVehicle (self):
        print('Datos del Vehiculo'.center(100, '-') + '\n')
        print('El nombre del vehiculo es: '+ self.nombre )
        print(f'El modelo de {self.nombre} es: {self.modelo}')
        print(f'El pais de {self.nombre} es : {self.pais}')
        print(f'La velocidad de {self.nombre} es: {self.velocidad}')
        print(f'El tipo de {self.nombre} es : {self.tipo}')
        print(f'El color de {self.nombre} es: {self.color}')

    #Todos los metodos set de la clase:
    def setNombre(self, nombre):
        self.nombre = nombre

    def setModelo(self, modelo):
        self.Modelo = modelo
    def setPais(self, pais):
        self.pais = pais

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def setTipo(self, tipo):
        self.tipo = tipo
    def setColor(self,color):
        self.color = color

    #Ahora todos los metodos get:

    def getNombre (self):
        return self.nombre

    def getModelo (self):
        return self.modelo

    def getPais (self):
        return self.pais

    def getVelocidad (self):
        return self.velocidad

    def getTipo(self):
        return self.tipo

    def getColor (self):
        return self.color


##coche = vehicle('Lamborgini','G200','Italiano','320km/h','Deportivo','Rojo')
#coche.dadesVehicle()

class animal:
    def __init__(self,nombre,peso,altura,velocidad,pais,color):
        self.nombre= nombre
        self.peso= peso
        self.altura = altura
        self.velocidad =velocidad
        self.pais= pais
        self.color= color
    def salutacio (self):
        print('Datos del animal'.center(100, '-') + '\n')
        print('El nombre del animal es: '+ self.nombre )
        print(f'El peso de {self.nombre} es: {self.peso}')
        print(f'La altura de {self.nombre} es: {self.altura}')
        print(f'La velocidad de {self.nombre} es: {self.velocidad}')
        print(f'El pais de {self.nombre} es : {self.pais}')
        print(f'El color de {self.nombre} es: {self.color}')

    #Todos los metodos set de la clase:
    def setNombre(self, nombre):
        self.nombre = nombre

    def setPeso(self, peso):
        self.peso = peso

    def setAltura(self, altura):
        self.altura = altura

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def setPais(self, pais):
        self.pais = pais
    def setColor(self,color):
        self.color = color

    #Ahora todos los metodos get:

    def getNombre (self):
        return self.nombre
    def getPeso (self):
        return self.peso
    def getAltura (self):
        return self.altura
    def getVelocidad (self):
        return self.velocidad
    def getPais (self):
        return self.pais
    def getColor (self):
        return self.color


#animal1 = animal('Tigre','15kg','0.50m','120km/h','Tanzania','Amarillo y negro')
#animal1.salutacio()

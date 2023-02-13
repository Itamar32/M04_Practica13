"""Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user.
Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
"""
class user: #Aquí creamos la clase
    def __init__(self, nombre,apellido1,apellido2,edad,estatura,asignatura): #Se definen los atributos de la clase
        self.nombre= nombre #Aquí definimos las instancias de los atributos
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.edad=edad
        self.estatura=estatura
        self.asignatura=asignatura


    def salutacio(self): #Aquí definimos el método principal haciendo llamadas a las instancias de la clase
        print("Hola mi nombre es "+self.nombre +"\n el primer apellido es " + self.apellido1 + "\n y el segundo apellido es "+self.apellido2+ "\n la edad es " + self.edad +
        "\n la estatura es " + self.estatura + "\n y por último la asignatura cursada es "+ self.asignatura)

    """A partir de aquí definimos los getters y setters de los atributos de la clase. Esto sirve para poder ver el valor de la tributo(getters)
    y para cambiar la instancia de los atributos por una instancia nueva (setters)"""
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getApellido1(self):
        return self.apellido1
    def setApellido1(self,apellido1):
        self.apellido1=apellido1
    def getApellido2(self):
        return self.apellido2
    def setApellido2(self,apellido2):
        self.apellido2=apellido2
    def getEdad(self):
        return self.edad
    def setEdad(self,edad):
        self.edad=edad
    def getEstatura(self):
        return self.estatura
    def setEstatura(self,estatura):
        self.estatura=estatura
    def getAsignatura(self):
        return self.asignatura
    def setAsignatura(self,asignatura):
        self.aisgnatura=asignatura
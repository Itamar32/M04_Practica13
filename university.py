"""Crear un arxiu de nom university.py. En aquest arxiu s’ha de crear una class de nom university. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom info on es mostren, per pantalla, totes les dades (atributs) de university.
"""
class university: #Aquí creamos la clase
    def __init__(self,clase,asignatura2,semestre,nota,matriculaHonor,recuperacion): #Se definen los atributos de la clase
        self.clase= clase  #Aquí definimos las instancias de los atributos
        self.asignatura2=asignatura2
        self.semestre=semestre
        self.nota=nota
        self.matriculaHonor=matriculaHonor
        self.recuperacion=recuperacion


    def info(self):  #Aquí definimos el método principal haciendo llamadas a las instancias de la clase
        print("La clase es la letra  "+self.clase +"\n y la asignatura es " + self.asignatura2 + "\n el semestre cursado es el "+self.semestre+ "\n la nota obtenida es " + self.nota +
              "\n ¿ Es una matricula de honor ? " + self.matriculaHonor + "\n ¿Debe recuperar la asignatura? "+ self.recuperacion)

    """A partir de aquí definimos los getters y setters de los atributos de la clase. Esto sirve para poder ver el valor de la tributo(getters)
    y para cambiar la instancia de los atributos por una instancia nueva (setters)"""
    def getClase(self):
        return self.clase
    def setClase(self,clase):
        self.clase=clase
    def getAsignatura2(self):
        return self.asignatura2
    def setAsignatura2(self,asignatura2):
        self.asignatura2=asignatura2
    def getSemestre(self):
        return self.semestre
    def setSemestre(self,semestre):
        self.semestre=semestre
    def getNota(self):
        return self.nota
    def setNota(self,nota):
        self.nota=nota
    def getMatriculaHonor(self):
        return self.matriculaHonor
    def setMatriculaHonor(self,matriculaHonor):
        self.matriculaHonor=matriculaHonor
    def getRecuperacion(self):
        return self.recuperacion
    def setRecuperacion(self,recuperacion):
        self.recuperacion=recuperacion
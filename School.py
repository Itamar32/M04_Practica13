class school:
    def __init__(self, nombre, ciudad, especialidad, año, numProf, numAlum):
        self.nombre = nombre
        self.ciudad = ciudad
        self.especialidad= especialidad
        self.año= año
        self.numProf = numProf
        self.numAlum = numAlum
    def datosColegio (self):
        print('Datos del colegio'.center(100,'-')+'\n')
        print('El nombre del colegio es: '+ self.nombre )
        print(f'El {self.nombre} esta en: {self.ciudad}')
        print(f'La es especialidad de {self.nombre} es : {self.especialidad}')
        print(f'El año de construccion de {self.nombre} es: {self.año}')
        print(f'Numero de profesores: {self.numProf}')
        print(f'Numero de alumnos: {self.numAlum}')

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCiudad(self,ciudad):
        self.ciudad = ciudad

    def setEspecialidad(self,especialidad):
        self.especialidad= especialidad

    def setAño(self,año):
        self.año = año

    def setNumPro(self,numProf):
        self.numProf = numProf

    def setNumAlum(self,numAlum):
        self.numAlum =numAlum

    def getNombre(self):
        return self.nombre
    def getCiudad(self):
        return self.ciudad
    def getEspecialidad(self):
        return self.especialidad
    def getAño(self):
        return self.año
    def getNumProf(self):
        return self.numProf
    def getNumAlum(self):
        return self.numAlum


#cole1 = school('Jaume Balmes','Barcelona','Programación','1975','26','1192')
#cole1.datosColegio()


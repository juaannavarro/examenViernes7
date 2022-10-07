class alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre, self.nota)
    def comprobacion(self):
        if self.nota >= 5:
            print( "Aprobado")
        else:
            print ("Suspenso")
    def crear_alumno():
        nombre = input("Nombre: ")
        nota = int(input("Nota: "))
        print("Alumno creado: ", alumno(nombre, nota))
        print("Comprobacion de la nota")
        print( alumno.comprobacion(alumno(nombre, nota)))
alumno.crear_alumno()


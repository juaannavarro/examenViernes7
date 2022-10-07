class alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre, self.nota)
    def comprobacion(self):
        if a >= 5:
            print( "Aprobado")
        else:
            print ("Suspenso")


a = alumno("Juan", 5)
print(a)
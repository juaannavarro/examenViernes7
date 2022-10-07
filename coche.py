class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)



class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)
    
b = Bicicleta("roja", 2, "urbana")


class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", {} kg".format(self.carga)
    
C = Camioneta("verde", 4, 90, 2000, 500)


class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.tipo = tipo

    def __str__(self):
        return Coche.__str__(self) + ", {}".format(self.tipo)
    
m = Motocicleta("negra", 2, 180, 600, "deportiva")

def catalogar(vehiculos, ruedas):
    for v in vehiculos:
        print( v.__class__.__name__,v)
        if v.ruedas == ruedas:
            print("tiene {} ruedas".format(ruedas))
        else:
            print("no tiene {} ruedas".format(ruedas))
    
    h = int(input("Introduce el número de ruedas: "))
    if h == 2:
        catalogar([ b, m], h)
    elif h == 4:
        catalogar([c, C], h)
    elif h ==0:
        catalogar([c, b, C, m], h)
    else:
        print("No hay vehículos con {} ruedas".format(h))
    
catalogar([c, b, C, m],0)


            
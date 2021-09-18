class Animal:
    def __init__(self, peso):
        self.peso = peso
    
    def Comer(self):
        print("Comiendo..")

class Oviparo(Animal):
    def __init__(self, peso):
        Animal.__init__(self, peso)

    def ponerHuevos(self):
        print("Poniendo huevos..")

class Mamifero(Animal):
    def __init__(self, peso):
        Animal.__init__(self, peso)

    def tipSangre(self, sangreCaliente):
        self.sangreCaliente = sangreCaliente
        if(self.sangreCaliente):
            print("Sangre Caliente")
        else:
            print("Sangre Fria")
    
    def Parir(self):
        print("Pariendo..")

    def Amamantar(self):
        print("Amamantando..")

class Delfin(Mamifero):
    def __init__(self, sangreCaliente):
        Mamifero.__init__(self, sangreCaliente)

    def Nadar(self):
        print("Nadando..")

class Perro(Mamifero):
    def __init__(self, colorPelo):
        self.colorPelo = colorPelo

    def Ladrar(self):
        print("Ladrando..")

#u1 = Oviparo("120g")
#print(u1.peso)
#u1.Comer()
#mamif = Mamifero("100g")
#print(mamif.peso)
#mamif.tipSangre(True)
#mamif.Comer()
#mamif.Parir()
#mamif.Amamantar()
#delf = Delfin("")
#delf.Nadar()
#delf.tipSangre(False)
#prr = Perro("Negro")
#print(prr.colorPelo)
#prr.tipSangre(True)
#prr.Ladrar()

class Operacion:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

class Suma(Operacion):
    def mostrarResultadoS(self):
        suma = self.n1 + self.n2
        resultado = suma
        print(resultado)

class Resta(Operacion):
    def mostrarResultadoR(self):
        resta = self.n1 - self.n2
        resultado = resta
        print(resultado)

class Multiplicacion(Operacion):
    def mostrarResultadoM(self):
        multiplicacion = self.n1 * self.n2
        resultado = multiplicacion
        print(resultado)

class Division(Operacion):
    def mostrarResultadoD(self):
        division = self.n1 / self.n2
        resultado = division
        print(resultado)

calculoS = Suma(2, 3)
calculoS.mostrarResultadoS()
calculoR = Resta(2, 3)
calculoR.mostrarResultadoR()
calculoM = Multiplicacion(2, 5)
calculoM.mostrarResultadoM()
calculoD = Division(2, 4)
calculoD.mostrarResultadoD()


    



    



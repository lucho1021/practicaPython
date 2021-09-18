class Persona:
    def __init__(self, nombre, edad, peso, estatura, colorOjos, sexo):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.colorOjos = colorOjos
        self.sexo = sexo

    def comer(self):
        print("Comiendo..")
    
    def correr(self):
        print("Corriendo")

    def tomar(self):
        print("Tomando..")

    def dormir(self):
        print("Durmiendo..")

    def despertar(self):
        print("Despertando..")

    def bailar(self):
        print("Bailar..")

class Veterinario(Persona):
    def __init__(self, nombre, edad, peso, estatura, colorOjos, sexo, cedula, especialidad):
        Persona.__init__(self, nombre, edad, peso, estatura, colorOjos, sexo)
        self.cedula = cedula
        self.especialidad = especialidad

    def consultar(self):
        print("Consultar..")

    def encirugia(self):
        print("En cirugia..")

class Abogado(Persona):
    def __init__(self, nombre, edad, peso, estatura, colorOjos, sexo, titulo, curso):
        Persona.__init__(self, nombre, edad, peso, estatura, colorOjos, sexo)
        self.titulo = titulo
        self.curso = curso

    def litigar(self):
        print("Defensor de partes involucradas..")

abogadito1 = Abogado("Luis", "17", "57kg", "1.64", "Negros", "M", "Nn", "4to")
print(abogadito1.nombre)
abogadito1.litigar()
Veterinario1= Veterinario("Miguel", "17", "57kg", "1.64", "Negros", "M", "1025640778", "ASD")
print(Veterinario1.nombre)
Veterinario1.bailar()



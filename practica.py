#puntoA

"""factorial = input ('ingresa un numero ')

factorial = int (factorial)

def calculafactorial(factorial):

    if factorial==0 or factorial==1:
            resultado=1
    elif factorial > 1:
            resultado=factorial*calculafactorial(factorial-1)
    return resultado


print("el factorial de",factorial ,"es: ",calculafactorial(factorial))"""



# puntoB

"""num = input('ingresa un numero ')

num = int(num)

def calcularFibonacci(num):
    i = 0
    n1 = 0
    n2 = 1
    for i in range(num):
       print(num, end=' ')
       num = (num-1) + (num-2)
    return num

print(calcularFibonacci(num))"""


    #puntoC

"""
prestamo = int(input("Ingresa el valor del prestamo: "))

cuota = int(input("Ingresa el total de cuotas a pagar: "))

def calcularcuotavalor(prestamo, cuota):
    resultadocuota = prestamo / cuota
    tasamensual = resultadocuota * 0.03
    resultadoT = resultadocuota + tasamensual
    return resultadoT

print("El total a pagar cada cuota es de: ",calcularcuotavalor(prestamo,cuota))
"""

    #puntoD

"""
mostrardatos = ["hola", "asd", 13]

print(mostrardatos)
"""

    #puntoE

"""
diccionario = {"saludo": "hola", "pregunta": "¿?"}
print (diccionario["saludo"])
"""

    #puntoF

"""
dpagos = {"placa": "tis123", "marca": "Aveo", "pagos":[100,200,30,400]}

print (sum(dpagos["pagos"]))
"""

    #Punto3

"""
ciudad = "medellín"
pais = "colombia"
lugar = "el salvador"

diccionario2 = {
    ciudad,
    pais,
    lugar
}
print(diccionario2)
"""

    #punto4

"""
datos = int(input("Ingresa la cantidad de datos a ingresar como 50: "))
i = 1

while i <= datos:
    print(i)
    i += 1 
"""

"""
dato = int(input("Ingrese cantidad de numeros: "))
lista = []
count = 0

while count < dato:
    count +=1
    lista.append(count)

print((lista))
"""

    #punto5
    
"""
datosimp = int(input("Ingresa la cantidad de datos a ingresar para mostrar numeros negativos: "))
i = 1

while i <= datosimp:
    print(i)
    i += 1 * 2   
"""

    #punto6

"""
vehiculo = {
    "placa":"123-asd",
    "marca":"tesla",
    "modelo":"2020",
    "valor":200000
}
print(vehiculo)
"""

    #Otro metodo de hacer

"""
cantVehiculos = int(input("Ingresa la cantidad de vehiculos a registrar: "))

vehiculo = {}

for n in range(cantVehiculos):
    placa = int(input(f"Ingresa la placa del vehiculo {n + 1}: "))
    marca = int(input(f"Ingresa la marca del vehiculo {n + 1}: "))
    modelo = int(input(f"Ingresa el modelo del vehiculo {n + 1}: "))
    valor = int(input(f"Ingresa el valor del vehiculo {n + 1}: "))
    vehiculo = {"placa":placa, "marca":placa, "modelo":placa, "valor":placa}
    print(vehiculo)
"""

    #Punto8

"""
ciudades = []

ciudad = int(input("Ingresa cantidad de ciudades: "))

for i in range(ciudad):
    ciudad = input(f"Digita la ciudad {i + 1}: ")
    ciudades += [ciudad]
print(ciudades)

    #Punto9 y 10

agregarCiudad = (input("Ingresa la ciudad por agregar: "))

ciudades.append(agregarCiudad)

print(ciudades)

    #punto11

eliminarCiudad = input("Ciudad a eliminar: ")

for i in range(len(ciudades)-1, -1, -1):
    if ciudades [i] == eliminarCiudad:
        del ciudades[i]
print(f"Las ciudades ahora es: {ciudades}")
"""











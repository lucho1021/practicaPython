#12. Crear una clase con los datos de un vehículo (placa, marca, modelo, precio). Los atributos son privados
#13. Instanciar un objeto de la clase vehículo
class vehiculo():
    def __init__(self, placa, marca, modelo, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def __repr__(self):
       return f"Placa: {self.placa}\nMarca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio}"
       
vehiculo1 = vehiculo('Placa', 'Marca', 'Modelo', 'Precio')
print(vehiculo1)
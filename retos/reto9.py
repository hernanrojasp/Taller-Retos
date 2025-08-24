class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

class Veterinaria:
    def checkup(self, animal):
        print(f"Realizando revisión a {animal.nombre}, que es un {animal.especie},y esta en buen estado de salud.")


perro = Animal("Nina", "perro")
gato = Animal("Asrael", "gato")

mi_veterinaria = Veterinaria()
mi_veterinaria.checkup(perro)
mi_veterinaria.checkup(gato)

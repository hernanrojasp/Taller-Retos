class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def feed(self):
        print(f"{self.name} el {self.species} esta comiendo.")


class Owner:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} el {animal.species} esta agregado a la lista de {self.name} Zoo.")

    def feed_all_animals(self):
        print(f"{self.name} esta alimentando a todos los animales:")
        for animal in self.animals:
            animal.feed()



owner = Owner("Hernan")
perro= Animal("Nina", "perro")
gato = Animal("Asrael", "gato")
pajaro = Animal("Piolin", "pajaro")
Loro = Animal("Rebecca", "loro")
aguila = Animal("Aguila Real", "aguila")

owner.add_animal(perro)
owner.add_animal(gato)
owner.add_animal(pajaro)
owner.add_animal(Loro)
owner.add_animal(aguila)

owner.feed_all_animals()

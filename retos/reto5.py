
class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"{self.__class__.__name__}: {self.name}"

class Dog(Animal):
    def bark(self):
        return "Nina"

    def fetch(self, item):
        print(f"{self.name} ha traído el/la {item}!")

class Cat(Animal):
    def meow(self):
        return "Asrael"

    def sleep(self):
        print(f"{self.name} está durmiendo la siesta")

class Bird(Animal):
    def chirp(self):
        return "Piolin"

class Parrot(Bird):
    def talk(self, phrase):
        print(f"{self.name} dice: '{phrase}'")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        print("Animales en el zoológico:")
        for animal in self.animals:
            print(animal.show_info())

if __name__ == "__main__":
    zoo = Zoo()
    perro = Dog("Nina")
    gato = Cat("Asrael")
    pajaro = Bird("Piolín")
    loro = Parrot("Rebecca")

    zoo.add_animal(perro)
    zoo.add_animal(gato)
    zoo.add_animal(pajaro)
    zoo.add_animal(loro)

    zoo.show_animals()


    perro.fetch("Rama")
    gato.sleep()
    loro.chirp()
    loro.talk("quiero cacao")


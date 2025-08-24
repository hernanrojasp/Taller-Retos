
class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"{self.__class__.__name__}: {self.name}"

class Dog(Animal):
    def bark(self):
        return "Woof!"

    def fetch(self, item):
        print(f"{self.name} ha traído la {item}!")

class Cat(Animal):
    def meow(self):
        return "Miau!"

    def sleep(self):
        print(f"{self.name} está durmiendo la siesta")

class Bird(Animal):
    def chirp(self):
        return ""

class Parrot(Bird):
    def talk(self, phrase):
        print(f"{self.name} dice: '{phrase}'")

class Eagle(Bird):
    def __init__(self, name, altitude=0):
        super().__init__(name)
        self.altitude = altitude

    def show_altitude(self):
        print(f"{self.name} está volando a {self.altitude} metros de altitud.")


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
    aguila = Eagle("Águila Real", 1500)

    zoo.add_animal(perro)
    zoo.add_animal(gato)
    zoo.add_animal(pajaro)
    zoo.add_animal(loro)
    zoo.add_animal(aguila)

    zoo.show_animals()

    
    perro.fetch("Rama")
    gato.sleep()
    loro.chirp()
    loro.talk("quiere cacao")
    aguila.show_altitude()

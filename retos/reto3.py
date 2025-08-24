
class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"{self.__class__.__name__}: {self.name}"

class Dog(Animal):
    def nina(self):
        return "Nina"

class Cat(Animal):
    def Asrael(self):
        return "Asrael"

class Bird(Animal):
    def piolin(self):
        return "Piolin"

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
    zoo.add_animal(Dog("Nina"))
    zoo.add_animal(Cat("Asrael"))
    zoo.add_animal(Bird("Piolín"))

    zoo.show_animals()

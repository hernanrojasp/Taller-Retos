class Fish:

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def swim(self):
            print(f"{self.name} el pez esta en el mar!")

if __name__ == "__main__":
    nemo = Fish("Nemo", 2, "Clownfish")
    dory = Fish("Dory", 3, "Blue Tang")

    nemo.swim()
    dory.swim()
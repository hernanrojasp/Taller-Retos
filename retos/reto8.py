class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_dog):
        if self.age > other_dog.age:
            return f"{self.name} es mayor que {other_dog.name}."
        elif self.age < other_dog.age:
            return f"{other_dog.name} es mayor que {self.name}."
        else:
            return f"{self.name} y {other_dog.name} tienen la misma edad."


dog1 = Dog("Nina", 3)
dog2 = Dog("Pecas", 3)

print(dog1.compare_age(dog2)) 

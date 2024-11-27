from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def make_sound(self):
        pass


# interface -> rozhranie
class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass

# mixin
class Dychanie:
    def dycham(self):
        print("dycham")


class Dog(Dychanie, Walkable, Animal):
    def make_sound(self):
        print("I am a dog.")

    def walk(self):
        print("dog is walking")


class Cat(Walkable, Animal):
    def make_sound(self):
        print("I am a cat.")

    def walk(self):
        print("cat is walking")


class Fish(Animal):
    def make_sound(self):
        print("I am a fish.")


#a = Animal("Bob")
animals: [Animal] = [Dog("Dunco"), Cat("micka"), Fish("Rybka")]

print(Dog.mro())

for animal in animals:
    animal.make_sound()
    if isinstance(animal, Walkable):
        animal.walk()
    else:
        print("I don't know how to do that.")
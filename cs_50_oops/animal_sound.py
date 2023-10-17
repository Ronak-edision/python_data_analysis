from abc import ABC, abstractmethod 

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("woff")

class Cat(Animal):
    def sound(self):
        print("meow")

class Cow(Animal):
    def sound(self):
        print("moow")

dog= Dog()
dog.sound()


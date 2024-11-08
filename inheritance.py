# Parent Class
class Animal:
    def speak(self):
        print('Animal is speaking')


# Child Class
class Dog(Animal):
    def bark(self):
        print('Dog is barking')

class Cat(Animal):
    def meow(self):
        print('Cat is meowing')


a = Animal()
b = Dog()
c = Cat()




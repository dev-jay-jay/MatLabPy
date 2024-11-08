class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def move(self):
        print('Person is walking')


a = Person('JJ', 19, 'F')
b = Person('Jane', 25, 'F')
c = Person('Joe', 22, 'M')

print(a.name, a.age, a.gender)
print(b.name, b.age, b.gender)



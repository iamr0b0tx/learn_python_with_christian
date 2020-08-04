'''
Getting started with OOP
 - what is OOP?
 - why OOP?
 - class vs instance?
 - writing a class
 - creating an object
 - class vs instance variables
 - inheritance and polymorphism
'''

class Animal:
    def make_sound(self):
        print("Animal making sound!")

    def move(self):
        print("i am a moving animal!")


animal = Animal()
animal.make_sound()
animal.move()

class Dog(Animal):
    def make_sound(self):
        print("bark!")


dog = Dog()
dog.make_sound()
dog.move()

class Cat(Animal):
    def make_sound(self):
        print("meow!")


cat = Cat()
cat.make_sound()
cat.move()
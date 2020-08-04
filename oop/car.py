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

class Calculator:
    def __init__(self, name):
        ''' this is the constructor, it is option '''
        self.make = maker
        self.model = year
        self.color = color

    def move(self):
        print(f"{self.make} is moving")

    def start(self):
        print(f"{self.make} is starting...")

    def reverse(self):
        print(f"{self.make} is reversing..")


nissan = Car("Nissan", "2019", "red")
nissan.start()
nissan.move()

mazda = Car("Mazda", "2018", "dim blue")
mazda.start()
mazda.move()
mazda.reverse()

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
        self.name = name

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2


casio = Calculator("Casio")
purpo = Calculator("purpo")

result = casio.add(2, 3)
print(result)

result_p = purpo.add(10, 15)
print(f"purpo result is {result_p}")

result = casio.subtract(result, 2)
print(result)


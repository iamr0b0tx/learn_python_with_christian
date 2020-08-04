class Animal:
    def __init__(self):
        self.color = None
        self.height = None
        self.weight = None

    def move(self):
        print("Animal is Moving!")

    def eat(self):
        print("Animal is eating!")
    
    def make_sound(self):
        print("Animal is making sound!")


class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# initialize a dog/cat instance
skipi = Dog()
kitty = Cat()

# calling methods of the instance
skipi.make_sound()
kitty.make_sound()


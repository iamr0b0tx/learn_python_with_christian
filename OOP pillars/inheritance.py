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
    pass

# initialize a dog instance
skipi = Dog()

# calling methods of the instance
skipi.move()
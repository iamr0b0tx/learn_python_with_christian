
class Car:
    def __init__(self, n, m):
        print(n, m)
    def setColor(self, color):
        self.color = color
        return self

    def setName(self, name):
        self.name = name
        return self


    @classmethod
    def new_car(cls, n, m):
        return cls(n, m)
if __name__ == "__main__":
    c1 = Car(4, 6)
    Car.new_car(1, 2)

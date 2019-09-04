
class Car:
    def run(self):
        print('car is running')
        return self

    def noise(self):
        print('car is making noise')
        return self

if __name__ == "__main__":
    c1 = Car()
    c1.run().noise()

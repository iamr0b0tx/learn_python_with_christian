from point import Point

class Square:
    def __init__(self, p1, p2, p3, p4):
        #initilize the vertices
        self.p1, self.p2, self.p3, self.p4 = p1, p2, p3, p4

        #get the length of the side
        self.initializeLength()

        #properties of square
        self.perimeter = None
        self.area = None

    def initializeLength(self):
        '''get the length of a side the square'''
        self.length = self.p1.distance(self.p2)
        
    def getPerimeter(self):
        '''calc perimeter of the square'''
        if self.perimeter is None:
            self.perimeter = 4*self.length
        return self.perimeter

    def getArea(self):
        '''calc the area of the square'''
        if self.area is None:
            self.area = self.length**2
        return self.area

    def __str__(self):
        return f'Length of side: {self.length}\nPerimeter: {self.perimeter}\nArea: {self.area}\n'

def main():
    print('square.py function is running')
    p1, p2, p3, p4 = [Point(i, i) for i in range(4)]

    for p in [p1, p2, p3, p4]:
        print(p)
    print()

    sq1 = Square(p1, p2, p3, p4)

    print(sq1)

    sq1.getPerimeter()
    print(sq1)

    sq1.getArea()
    print(sq1)
    
    print('square.py function is done')
    
if __name__ == '__main__':
    main()


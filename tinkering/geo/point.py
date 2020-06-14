##import square root from math
from math import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0):
        '''construct a point instance'''
        self.x = x
        self.y = y

    def distance(self, another_point):
        '''calc distance between two points'''
        x_dist = self.x - another_point.x
        y_dist = self.y - another_point.y
        return sqrt(x_dist**2 + y_dist**2)

    def __str__(self):
        '''str representation of the object'''
        return f'Point ({self.x}, {self.y})'
    
def main():
    #init class
    p1 = Point(1,1)
    p2 = Point(2,2)

    print('point.py main function is running')
    print(p1)
    print(p2)
    print('point.py main function is done\n')
    
if __name__ == '__main__':
    main()


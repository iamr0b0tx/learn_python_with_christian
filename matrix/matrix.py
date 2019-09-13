from utils import *

class Matrix:
    def __init__(self, li):
        self.matrix = li
        raise
            
    def validate(self):
        length_of_value = None
        for value in self.matrix:
            if length_of_value is None:
                length_of_value = find_length(value)
            else:
                if length_of_value != find_length(value):
                    return False     
        return True

    def __str__(self):
        return f'{self.matrix}'

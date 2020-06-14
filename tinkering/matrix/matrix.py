from utils import *

class Matrix:
    def __init__(self, li):
        self.matrix = li
        if self.validate() == False:
            raise ValueError('Invalid dimension!')
    
    def add(self, matrix_object):
        '''adds two matrix and returns the sum'''
        A = self.matrix
        B = matrix_object.matrix

        matrix_sum = [[0 for _ in x] for x in A] #array[3][3]
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                matrix_sum[i][j] = A[i][j] + B[i][j]

        return matrix_sum

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
        if find_length(self.matrix[0]) == 0:
            return f'{self.matrix}'
        
        else:
            rep = 'Matrix => [\n'
            for a in self.matrix:
                rep += ' ['
                for b in a:
                    rep += str(b)+ ' '
                
                rep = rep.strip()
                rep += ']\n'
            rep += ']\n'
            
            return rep
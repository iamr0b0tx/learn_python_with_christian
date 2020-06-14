from matrix import Matrix

'''
A =>
[ 1, 2, 3]
[ 4, 5, 6]
[ 7, 8, 9]
'''

def main():
    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    # B = Matrix([1,2,3])
    # C = Matrix([1, [2, 3]])
    B = Matrix([[10, 2, 3], [4, 50, 6]])


    print(A)
    print(B)
    print(A.add(B))


if __name__ == '__main__':
    main()

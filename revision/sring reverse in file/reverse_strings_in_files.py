def strFileReverse(filepath):
    #file to read from
    file_object = open(filepath, 'r')

    #file to write to
    file_object2 = open('rev_strings.txt', 'w')

    for line in file_object:
        print(line[::-1], file=file_object2)

    file_object.close()
    file_object2.close()

strFileReverse('statements.txt')
    

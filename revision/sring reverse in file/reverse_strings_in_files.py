def strFileReverse(filepath):
    #file to read from
    file_object = open(filepath, 'r')

    #file to write to
    file_object2 = open('rev_strings.txt', 'w')

    file_object3 = open('rev_strings2.txt', 'w')
    

    for line in file_object:
        output = ' '.join(line.split()[::-1])
        
        print(output, file=file_object2)

        file_object3.write(output+ '\n')

    file_object.close()
    file_object2.close()
    file_object3.close()

strFileReverse('statements.txt')

def readFile(filepath):
    file_object = open(filepath, 'r')
    
    content_list = file_object.readline()
    print(file_object.tell())

    file_object.readline()
    print(file_object.tell())
    
    file_object.close()

    print(content_list)
    
readFile('statements.txt')

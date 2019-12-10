##write a file
with open("cohort2/joshua.txt", 'w+') as fileObj:
    fileObj.write('I know too much')
    fileObj.seek(0)
    contents1 = fileObj.read()
    print(contents1)

    fileObj.write('Hello hello')
    fileObj.seek(0)
    contents2 = fileObj.read()
    print(contents2)

    fileObj.seek(10)
    fileObj.write('YES')
    fileObj.seek(0)
    contents3 = fileObj.read()
    print(contents3)

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__nin = 34567323

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} year(s)'

    def someMethod(self):
        pass



a_student = Student('James', 'Jack', 45)

'''
Author: Joshua Christian
Aim: To create a switch-case in python
Date: Sat, 27 jan 2018. 5:43pm

Summary
=======
This program's goal is to create a switch-case in python.

All these information you read in between the three apostrophes and the ones that start with '#' are ignored by the interpreter.
This mean they are not read or run as python code. They can be reffered to as comments, they are basically like a label for the programmer
to be able to understand his/her code even after a long time.

The program begings from the __name__ == __main__ line, this is where the interpreter initiates the program,
then the 'runProgram' function is exceuted(line after line),
input is collected from the user and stored in the variable 'nationality',
the switch class is instantiated,
cases are tested

'''


#definition of switch class
class Switch:
    #switch class constructor: runs when instanced of code is created
    def __init__(self, variable):
        self.variable = variable

    #method 'case' of the 'switch' class: if variable contains a case value then run a specifies set of instructions( function 'callback_function')
    def case(self, value, callback_function, *args):
        if self.variable == value:
            return callback_function(args)

    #method 'default' of the 'switch' class: for any case value
    def default(self, callback_function, *args):
        return callback_function(args)

#definition of function 'doThis' to hold set of instructions           
def doThis(arg_list):
    string = arg_list[0]
    print(string)
    
def runProgram():
    #program takes in a nationality and check cases of different nationalities and run different instructions for all
    nationality = input('Please type in your nationality: ')

    switch = Switch(nationality)
    switch.case('American', doThis, "How ya doin'?")
    switch.case('Nigerian', doThis, "How una dey?")
    switch.case('English', doThis, "How are you mate?")
    switch.default(doThis, "Hello?")


#program initiates from here
if __name__ == '__main__':
    #interpreter executes the function 'runProgram'
    runProgram()

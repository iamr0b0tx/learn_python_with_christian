##import the random integer generator
from random import randint

##collect the value to find square root of
value = int(input('Enter value: '))

##guess a square root
guess = randint(1, value)

##the closeness of the square root to actual value
difference = value

##keep running until closeness is achieve
while difference > 0.0001:
    #display the square root value
    print('Your guess is', guess)

    #find the quotient
    quotient = value / guess

    #find the avrerage value
    average = (quotient + guess) / 2

    #the closeness
    difference = abs(guess - average)

    #update the guess
    guess = average

#display the square root value
print('Your square root is %0.2f'%guess)

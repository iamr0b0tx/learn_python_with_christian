from random import randint

guess = randint(0, 100)
gameState = True

while gameState is True:
    num = int(input('Guess a number between 1 and 100: '))
    
    if num == guess:
        print('You guessed right')
        print('\nNew Game=============')
        guess = randint(0, 100)

    elif num == -1:
        print('Game Over!')
        gameState = False
                
    elif num > guess:
        print('Too high')

    else:
        print('Too low')

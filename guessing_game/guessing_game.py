##import the random number gen
from random import randint

##get the random number between 1 and 100 inclusive
random_number = randint(1, 100)

##the counter for tracking trials
counter = 0

##start the game loop
while True:
    #update the number of trials
    counter += 1

    #get the players guess
    guess = int(input('Guess a Number from 1 to 100: '))

    #if the guess in range of 1 and 100
    if 1 <= guess <= 100:

        #if the guess is same as random number
        if guess == random_number:
            #End the game
            print(f'You guessed RIGHT!! After {counter} attempt(s)')
            break

        #get the distance away from the random number
        distance = abs(guess - random_number)

        #if on the first trial
        if counter == 1:
            #and the distance is only 10  steps away, say WARM
            if distance <= 10:
                print('WARM!')

            #and the distance is over 10steps away, say COLD
            else:
                print('COLD!')

        #in subsequent trials
        else:
            #if close now than before, say WARMER
            if distance < last_distance:
                print('WARMER!')

            #if not
            else:
                print('COLDER!')

        #assign this distance to last distance for next iteration
        last_distance = distance

    #if out of range
    else:
        print('OUT OF BOUNDS!')

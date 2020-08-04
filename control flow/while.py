actual_number = 10
guess = None
number_of_guesses = 0

while actual_number != guess:
    guess = int(input("Type your guess: "))
    number_of_guesses += 1

print(f"You guessed it right after {number_of_guesses} trie(s)!")

# the initial query
query = None
FALLBACK_MESSAGE = "I am unable to respond to that!"
responses = {
    "hello": "Hi!",
    "hi": "Hello!",
    "how are you?": "I am Fine, Thank You!",
    "what is your name?": "ChrisBot",
    "how old are you?": "96",
    "what is your favourite food?": "A bit of Code :-)",
    "are you married?": "Error!"
}

# introduction
print(
    "Hello there!\nI am ChrisBot and I will like to be your Friend!\nSimply type 'q' to quit the program"
)
# a continuous loop
while query != 'q':
    # collect the input and make it lower case
    query = input('\_> ').lower()

    if query == 'q':
        print('Bye!')
        break

    # if the query in responses
    if query in responses:
        response = responses[query]
        print('\=>', response)

    else:
        # when no response available print FALLBACK_MESSAGE
        print(FALLBACK_MESSAGE)

    # to leave an empty line after the response
    print()

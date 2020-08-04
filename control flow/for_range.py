# when one arg is provided it is the stop parameter
print(list(range(10)))

# when two args are provided it is the start and stop that takes them respectively
print(list(range(1, 10)))

# when three args are provided it is the start, stop and step args that takes them respectively
print(list(range(1, 10, 2)))

for number in range(1, 10, 2):
    print("my current number is", number)
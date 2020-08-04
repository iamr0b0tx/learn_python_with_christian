values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
other_values = [3, 5, 1, 4, 7, 2]
other_new_values = [5,1,4,56,3,22]

def mean(values):
    total = 0
    num_of_values = 0
    for value in values:
        total += value
        num_of_values += 1

    mean_of_values = total / num_of_values
    return mean_of_values

print("mean of values is", mean(values))
print("mean of other values is", mean(other_values))
print("mean of other new values is", mean(other_new_values))

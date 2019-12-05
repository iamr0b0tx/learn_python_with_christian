##list initilized
my_list = [5, 1, 4, 2, 8]
list_size = len(my_list)

##display the initial list configuration
print(my_list)

##initialize swapped so the while loop can run
swapped = True

##repeat
while swapped:
    #no swap yet
    swapped = False

    #picks a pair of indices
    for current_index in range(1, list_size):
        prev_index = current_index - 1

        #get the values of the pair
        prev_value, current_value = my_list[prev_index], my_list[current_index]

        #if the prev is greater, swap them
        if prev_value > current_value:
            my_list[prev_index:current_index+1] = current_value, prev_value

            #set swap to true and display list
            swapped = True
            print(my_list)

#display the list
print(my_list)

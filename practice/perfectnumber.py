num = int(input('Enter a number here: '))

sum_of_factors = 0

for value in range(1, num):
    if num%value == 0:
        sum_of_factors += value

if sum_of_factors == num:
    print('Perfect Number!')

elif sum_of_factors > num:
    print('Abundant Number!')

else:
    print('Deficient Number!')



def add(num1, num2, num3):
    answer1 = num1 + num2
    answer2 = answer1 + num3
    return answer2

print("Welcome to add add add!")
print("We add numbers here! whooo!")

first_value = int(input("Type in a number: "))
second_value = int(input("Type in another number: "))
third_value = int(input("Another One: "))

result = add(first_value, second_value, third_value)
print(result)

print("Hope it was worth it!")
print("Thanks for using the program!")
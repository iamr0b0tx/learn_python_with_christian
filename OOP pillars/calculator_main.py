from calculator import Calculator

# initialize object for abstraction
calculator = Calculator()

while True:
    print("Type:\n A for Addition\n S for Subtraction\n M for multiplication\n D for division\n")
    operation = input("What would you like to do?: ")
    print()

    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    if operation == "A":
        result = calculator.add(num1, num2)

    elif operation == "S":
        result = calculator.subtract(num1, num2)

    elif operation == "M":
        result = calculator.multiply(num1, num2)

    elif operation == "D":
        result = calculator.divide(num1, num2)

    else:
        print("Invalid operation")

    print(f"Your result is {result}\n")
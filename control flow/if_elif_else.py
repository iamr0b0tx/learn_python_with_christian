while True:
    score = float(input("Type your score: "))

    if score >= 75:
        print("Distinction!")

    elif score >= 65:
        print("Very good!")

    elif score >= 60:
        print("Good!")

    elif score >= 50:
        print("Fair")
    
    else:
        print("Bad!")
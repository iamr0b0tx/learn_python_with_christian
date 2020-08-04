# now we will discuss service type
def service_type_and_amount():
    service = input("What kind of service did you need? Oil Change, Tire Rotation, or Regular Maintenance?: ").lower()
    if "oil change" in service:
        print("service it takes 2 hours, cost, Mark will complete the service")

    elif "tire rotation" in service:
        print("service it takes 30 minutes, cost, Luke will complete the service")

    elif "regular maintenance" in service:
        print("service it takes 3 hours, cost, Lucy will complete the service")

    else:
        print(f"Sorry {service}, unfortunately we cannot service you at the moment")

while True:
    print("Hello")
    name = input("What is your name?")

    print(f"Great {name}, let's get started!")
    print("Please answer a few question about your car to allow us to better help you")
    print()

    year = input("What is the year of the car?: ")
    make = input("What is the make of the car?: ")
    model = input("What is the model of the car?: ")

    # this will be a set of strings to assist with gathering data for your service
    car = (f"{year} {make} {model}")

    # now that you know what car you can confirm that the information is correct.
    print()
    print(f"""To confirm you have a 
    year: {year} 
    make: {make} 
    model: {model} 
    is this correct? (yes or no)""", end='')

    # if statements help us direct the next lines of question
    confirmation_yes = input("> ")
    if confirmation_yes == "yes":
        print(f"Awesome {name}, let's continue.")
        break
        
    else:
        print("oh no, let's try this again.")
        # need to create go to loop back to car make model

# now we will discuss service type
service_type_and_amount()
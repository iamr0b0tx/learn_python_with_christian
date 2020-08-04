print("Hello")

print("What is your name?", end='')
name = input()

print(f"Great {name}, let's get started!")
print("Please answer a few question about your car to allow us to better help you")

print("What is the year of the car?", end='')
year = input()

print("What is the make of the car?", end='')
make = input()

print("What is the model of the car?", end='')
model = input()

# this will be a set of strings to assist with gathering data for your service
car = (f"{year} {make} {model}")

# now that you know what car you can confirm that the information is correct.
print(f"""To confirm you have a 
year: {year} 
make: {make} 
model: {model} 
is this correct? (yes or no)""", end='')

# if statements help us direct the next lines of question
confirmation_yes = input(">")
if confirmation_yes == "yes":
    print(f"Awesome {name}, let's continue.")
    
else:
    print("oh no, let's try this again.")
    # need to create go to loop back to car make model

# now we will discuss service type
def service_type_and_amount():
    print("What kind of service did you need? Oil Change, Tire Rotation, or Regular Maintenance?")
    
    next = raw_input("> ")
    if "oil change" in oil_change:
        how_much = int(oil_change)

    elif "tire rotation" in tire_rotation:
        how_much = int(tire_rotation)

    if "regular maintenance" in regular_maintenance:
        how_much = int(regular_maintenance)

    else:
        print(f"Sorry {name}, unfortunately we cannot service you at the moment")

# using floats for value since we are dealing with cash transactions
def how_much():
    oil_change = 25.00
    tire_rotation = 15.00
    regular_maintenance = 40.0
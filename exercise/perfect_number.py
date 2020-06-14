num = int(input("Type in a num: "))

total = 0
for counter in range(1, num):
    if num%counter == 0:
        print(counter, end=', ')
        total += counter

print('sum =', total)

if total == num:
    print("perfect Number")

elif total < num:
    print("Deficient Number")

else:
    print("Abundant Number")

from math import ceil

def f(li):
    new_li = []
    for i, x in enumerate(li):
        if i == 0:
            new_li.append(1)

        if i > 0:
            new_li.append(x + li[i-1])

        if i == len(li) - 1:
            new_li.append(1)
    return new_li

def f2(li):
    new_li = []

    length = len(li)
    starting_index = ceil(length/2) if length > 1 else 0

    is_even = bool(length%2==0)
    
    for i in range(starting_index, length):
        if i > 0:
            new_li.append(li[i] + li[i-1])

        if i == length - 1:
            new_li.append(1)

    if is_even:
        new_li = new_li[1:][::-1] + new_li

    else:
        new_li = new_li[::-1] + new_li

    return new_li


li = [1]
height = int(input('Height of triangle: '))

for _ in range(height):
    print('{:^70s}'.format(li.__str__()))
    li = f2(li)

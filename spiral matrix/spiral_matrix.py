def spiral(n):
    arr = [[0 for i in range(n)] for i in range(n)]
    a = 0
    b = -1
    ai = bi = None
    inc_val = "b"
    print(arr)
    for i in range(1, n**2, 1):
        print((i-1)%n, ((i-1)%n== 0), inc_val)
        if i > 1 and (i-1)%n== 0:
            if inc_val == "a":
                inc_val = "b"

            else:
                inc_val = "a"

        print(inc_val)
        if inc_val == "a":
            a += 1
            
        else:
            b += 1

        ai = a%4
        bi = b%4
        print("i = {}, ai = {}, bi = {}, inc_val = {}, mod = {}".format(i, ai, bi, inc_val, i-1))
        arr[ai][bi] = i
        print('ab', arr[ai][bi])
        print(arr)
        print()
    return arr

def main():
    input_val = input("Type in an Integer: ")
    while type(input_val) != int:
        try:
            input_val = int(input_val)

        except Exception as e:
            print("\nInvalid input")
            input_val = input("Type in an Integer: ")

    arr = spiral(input_val)
    print(arr)
    
if __name__ == "__main__":
    main()

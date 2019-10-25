def switch(value):
    return {
        'a': 'ada',
        'b': 'bay'
    }.get(value)

def main():
    print(switch('a'))

if __name__ == "__main__":
    main()
def get_length(array: list) -> int:
    length: int = 0

    for _ in array:
        length += 1

    return length


def get_sum(array: list) -> int:
    total: int = 0

    for num in array:
        total += num

    return total


def get_mean(array: list) -> float:
    total: int = get_sum(array)
    length: int = get_length(array)
    mean: float = total / length
    return mean


if __name__ == '__main__':
    example_array: list = [1, 2, 3, 4, 5, 6]

    print("length = {}".format(get_length(example_array)))
    print("sum = {}".format(get_sum(example_array)))
    print("mean = {:.2f}".format(get_mean(example_array)))

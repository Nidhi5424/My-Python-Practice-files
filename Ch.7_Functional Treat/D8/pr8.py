def filter_args(*args):
    strings = []
    numbers = []
    for item in args:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
    return tuple(strings), tuple(numbers)

print(filter_args(1, "apple", 3.5, "banana", 9))

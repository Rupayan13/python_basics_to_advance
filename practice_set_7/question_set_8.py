def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(1, 2, 3, 4, 5))  # Output: 15


def print_details(**kwargs):
    for key in kwargs.keys():
        print(f"{key}: {kwargs[key]}")


print_details(name="Alice", age=25, city="Delhi")

# numbers = [1, 2, 3, 4, 5]

# cube_of_numbers = list(map(lambda x: x**3, numbers))
# print(cube_of_numbers)  # Output: [1, 8, 27, 64, 125]


# numbers = [10, 11, 12, 13, 14]

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [10, 12, 14]

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# def logger(func):
#     def wrapper():
#         print("Function is being called")
#         func()

#     return wrapper


# @logger
# def say_hello():
#     print("Hello!")


# say_hello()

from time import time


def timer(func):
    def wrapper(n):
        start = time()
        result = func(n)
        end = time()
        print(f"Time taken: {end - start}")
        return result

    return wrapper


@timer
def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum(1000000))

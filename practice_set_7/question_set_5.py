class NegativeNumberError(Exception):
    pass


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    if num1 < 0 or num2 < 0:
        raise NegativeNumberError("Both numbers must be non-negative.")
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

"""
day = int(input("Enter the day of the week (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number.")
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
symbol = input("Enter a mathematical symbol (+, -, *, /): ")

match symbol:
    case "+":
        print(f"The sum is: {num1 + num2}")
    case "-":
        print(f"The difference is: {num1 - num2}")
    case "*":
        print(f"The product is: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The quotient is: {num1 / num2}")
        else:
            print("Error: Division by zero.")
    case _:
        print("Invalid mathematical symbol.")
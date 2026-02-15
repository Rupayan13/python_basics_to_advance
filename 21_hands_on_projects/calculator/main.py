try:
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))

    print(
        "Enter + for addition\nEnter - for subtraction\nEnter * for multiplication\nEnter / for division"
    )

    operator = input("Enter the operator :")

    match operator:
        case "+":
            print(f"The result of {num1} + {num2} is {num1+num2}")
        case "+":
            print(f"The result of {num1} - {num2} is {num1-num2}")
        case "+":
            print(f"The result of {num1} * {num2} is {num1*num2}")
        case "/":
            print(f"The result of {num1} / {num2} is {num1/num2}")
        case default:
            print(f"The is an error.")
except Exception as e:
    print("Please enter the correct value of num1 and num2")

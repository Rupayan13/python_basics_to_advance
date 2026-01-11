a = int(input("Enter a number between 1 to 10 :"))

match a:
    case 1:
        print("You won a charger.")
    case 3:
        print("You own $3.")
    case 6:
        print("You own a camera.")
    case _:
        print("Better luck next time.")
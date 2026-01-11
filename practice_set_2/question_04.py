# i = 1
# while i <= 10:
#     print(i)
#     i += 1

"""
is_password_correct = False

password = "Rupayan108@"

while not is_password_correct:
    user_password = input("Enter your password: ")
    if user_password == password:
        is_password_correct = True
        print("Access granted.")
    else:
        print("Incorrect password. Try again.")

"""

num = int(input("Enter a number :"))
rev = 0

while num != 0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10

print("Reversed number is:", rev)   
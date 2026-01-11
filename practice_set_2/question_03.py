# for i in range(1, 11):
#     print(i)

"""
num = int(input("Enter a number: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

"""
"""
sum = 0
for i in range(1, 101):
    sum +=i
print(sum)
"""

row = int(input("Enter the number of rows: "))
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print("\n")
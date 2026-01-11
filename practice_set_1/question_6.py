first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

# sum
sum_result = first_num + second_num
print(f"The sum of {first_num} and {second_num} is {sum_result}")

# difference
diff_result = first_num - second_num
print(f"The difference when {second_num} is subtracted from {first_num} is {diff_result}")

# product
prod_result = first_num * second_num
print(f"The product of {first_num} and {second_num} is {prod_result}")

# quotient
if second_num != 0:
    quot_result = first_num / second_num
    print(f"The quotient when {first_num} is divided by {second_num} is {quot_result}")
else:
    print("Error: Division by zero is not allowed.")
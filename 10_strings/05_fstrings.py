template = "Dear {}, you are awesome, take this {}$ bag."

a = "Rupayan"
a1 = 10000
b = "Shaon"
b1 = 20000

s1 = template.format(a, a1)
s2 = template.format(b, b1)
print(s1)
print(s2)

# F-strings
print(f"Dear {a}, you are awesome, take this {a1}$ bag.")
print(f"Dear {b}, you are awesome, take this {b1}$ bag.")

print(ord('A')) # ASCII value of A
print(chr(65)) # Character represented by ASCII value 65
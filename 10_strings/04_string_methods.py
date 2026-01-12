s = "hello world"  # strings are immutable

# s[0] = 'b'  # this will raise an error

a = len(s)
print(a)

print(s.upper(), s)
print(s.lower())
print(s.capitalize())
print(s.title())

text = " hello world "
print(text.strip())  # removes leading and trailing spaces
print(text.lstrip())  # removes leading spaces
print(text.rstrip())  # removes trailing spaces

new_text = "Python is fun"
print(new_text.find("is"))  # returns the starting index of the substring
print(new_text.replace("fun", "awesome"))  # replaces substring

fruits = "apple,banana,cherry"
print(fruits.split(","))  # splits the string into a list
print(",".join(["apple", "banana", "cherry"]))  # joins a list into a string

text_latest = "Python123"
print(text_latest.isalpha())  # Output: False
print(text_latest.isdigit())  # Output: False
print(text_latest.isalnum())  # Output: True
print(text_latest.isspace())  # Output: False
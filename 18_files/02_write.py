# Write to file called john_doe.txt
# It should contain the data about John Doe

f = open("john_doe.txt", "w")

str = """
Name: John Doe
Age: 30
Occupation: Software Developer
Location: New York City
Hobbies: Hiking, Reading, Traveling
"""

f.write(str)

f.close()

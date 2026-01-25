# Append to an existing file called john_doe.txt
# It should contain the data about John Doe's hometown

f = open("john_doe.txt", "a")

str = """
Hometown: Los Angeles
Favorite Food: Sushi
Pet: Dog
Favorite Sport: Basketball
"""

f.write(str)

f.close()

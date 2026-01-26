import requests

r = requests.get("https://api.github.com/users/rupayan13")

# print(r.text)

with open("rupayan13.txt", "w") as f:
    f.write(r.text)

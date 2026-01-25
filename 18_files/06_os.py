import os

a = os.listdir("dir")

print(a)
print(os.getcwd())
print(os.path.exists("dir"))
# os.remove("sample.txt") # It will only remove files not directories
os.rmdir("dir/sub")  # It will only remove empty directories

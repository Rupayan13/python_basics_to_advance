import shutil

# shutil.rmtree("dir")  # It will remove a directory and all its contents
# # Be cautious while using this function as it will delete everything inside the directory permanently

# shutil.copy("john_doe.txt", "john_doe_copy.txt")  # It will copy the file with a new name

shutil.move("john_doe_copy.txt", "dir/john_doe_moved.txt")  # It will move the file to the specified directory
import os

# The os.listdir() function takes a path as an argument and returns a 
# list of strings representing the names of all entries in the directory, 
# including both files and subdirectories.

downloads = os.listdir("/home/lou/Downloads")
print(downloads) 
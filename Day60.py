# Exercise 7 Solution

# Lecture 75

# We have to use OS Module Functions to clear the clutter

# pngegg.com 


# Suppose we have to images in a folder 



import os 

files = os.listdir("Your foder name")

os.rename("folder nane", "renamed folder name")

for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"folder name/{file}", f"folder name/{i}.png")
        i = i + 1
    


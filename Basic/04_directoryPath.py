import os

# Select the Directory whose content you want to list
directory = '/'

# Use the os module to list the directory content
contents = os.listdir(directory)

# Print the contents of the directory 
for item in contents : 
    print(item)
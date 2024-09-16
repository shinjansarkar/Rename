import os

def coverage(path_name, user_name):  # Function
    count = 1

    for filename in os.listdir(path_name):  # Iterate over the files in the folder
        old_name = os.path.join(path_name, filename)  # Set the old name
        new_name = os.path.join(path_name, user_name+"_" + str(count) + '.jpg')  # Set the new name and extension
        os.rename(old_name, new_name)  # Rename from old name to new name
        count += 1  # Iterate +1

# Get user input
path_name = input("Enter the path: ")
user_name = input("Enter the Username of the coverage member: ")

# Call the function
coverage(path_name, user_name)

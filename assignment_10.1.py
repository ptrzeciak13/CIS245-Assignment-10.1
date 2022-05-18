import os
import os.path

# Checking to see if location exisits, if not creating it.
def dir():
    isExist = os.path.exists(user_dir_location)
    if not isExist:
        os.makedirs(user_dir_location)

# Getting user input, writing new file or appending existing file.
def file_write():
    print("Please enter the following information")
    user_name = input("Name: ")
    user_address = input("Address: ")
    user_phone_number = input("Phone Number: ")
    user_data = [user_name, user_address, user_phone_number]
    joined_data = ",".join(user_data)
    filename = user_filename + ".txt"
    file_location = os.path.join(user_dir_location, filename)
    isfile = os.path.isfile(file_location)
    if isfile:
        with open(filename, 'a') as saveFile:
            saveFile.write("\n")
            saveFile.write(joined_data)
            saveFile.close()
    else:
        with open(filename, 'w') as saveFile:
            saveFile.write(joined_data)
            saveFile.close()
    
    print()
    print("Your file name is " + filename + ", and it contains the following;")
    print()
    readFile = open(filename, "r")
    print(readFile.read())
    readFile.close()


# Requesting users directory location.
user_dir_location = input("Please input your directory path: ")

print()

dir()

# Requesting the file name from the user.
user_filename = input("Please enter your file name: ")

print()

file_write()

print()
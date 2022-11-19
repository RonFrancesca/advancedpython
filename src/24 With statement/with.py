# file = open("dummy.txt", "r")
# data = file.readline()
# new_data = data + 2
# file.close()

# try:
#     file = open("dummy.txt", "r")
#     data = file.readline()
#     new_data = data + 2
# except TypeError as error:
#     print(error)
# finally:
#     print("Safely closing file")
#     file.close()

with open("dummy.txt", "r") as file:
    data = file.readline()
    new_data = data + 2

# the with statement is going to create a contest manager, which under the hood, implement the try, except and finally 
# construct, so to safely close the file even if an exception is going to be thrown.
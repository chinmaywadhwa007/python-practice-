# file handling
# soo this is where we open our file
import os
file = open("file_handling/hello.txt", "r")
data = file.read()
print(data)
file.close()


# file editing
file = open("file_handling/hello.txt", "w")
file.write("hi chinmay\n")
file.write("welcome to the file handling ")
file.close()

# reading the file this msg is for line by line
# readline() reads one line at a time and moves the file pointer (cursor) to the next line. Therefore, the next call to readline() starts reading from where the previous call ended.
file = open("file_handling/hello.txt", "r")
print(file.readline())
file.close()  # means releases the recources

file = open("file_handling/hello.txt", "r")
# this means we it will read all at once without opening the file
print(file.readlines())

file.close()


# now let's talk about the appending data in file handling
# means add new file without deleteing the existing file u have
# it can change the file without changing the file....
with open("file_handling/hello.txt", "a") as file:
    file.write("\nchinmaywadhwa 4656454646")


# check if the file exit or not in the folder
if os.path.exists("./file_handling/hello.txt"):
    print("it exit in the folder ")
else:
    print("it doesn't exit in the folder ")

# for removing the file

# os.remove("./hello.txt")

# for reading a file
file = open("file_handling/hello.txt", "r")
for x in file:
    print(x)
file.close()

#
count = 0
with open("file_handling/hello.txt", "r") as hello:
    for x in hello:
        count += 1
print("line", count)

# read the multiple files at the same time

search = ["hello.txt", "hi.txt", "se.txt"]
for file in search:
    if os.path.exists(file):
        print(f"{file} found")
    else:
        print(f"{file} not found ")

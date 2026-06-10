# file handling
# soo this is where we open our file
file = open("file_handling/hello.txt", "r")
data = file.read()
print(data)
file.close()


# file editing
file = open("file_handling/hello.txt", "w")
file.write("hi chinmay\n")
file.write("welcome to the file handling ")
file.close()

# reading the file 
file=open("file_handling/hello.txt","r")
print(file)
# Print elements of a tuple
t = (1, 2, 3, 4, 5)
for i in t:
    print(i, end=" ")

 # Print numbers from 1 to 10 with while loop
i = 1
while i <= 10:
    print(i)
    i += 1

    # factorial of the number

n = int(input("ennter the number to find factorial : "))
fact = 1
i = n
while i >= 1:
    fact *= i
    i -= 1
    print("factorial of  the given number is :", fact)

# Sum of digits of a number
# n = int(input("enter a number:"))
# total = 0
# while n > 0:
#     total = total+n % 10
#     n //= 10
# print(total)


# factorial of the number
# taking input from the user inputs takes the user and int() converts into strings
a = int(input("Enter your number: "))
# this will intialzing the factorial variable
fact = 1
# this will run as a loop in python if user enter the value 5 this wll run till it gets the 5
while a >= 1:
    # fact*=a means fact = fact*a
    fact *= a
    # this means a=a-1
    a -= 1

print("Factorial is:", fact)

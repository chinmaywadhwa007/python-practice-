# -----------------------------
# Sum of digits of a number
# -----------------------------
# n = int(input("Enter the number: "))

# total = 0

# while n > 0:
#     total = total + n % 10
#     n //= 10

# print("Sum of digits:", total)


# -----------------------------
# Reverse a number
# -----------------------------
# n = int(input("Enter your number: "))

# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a //= 10

# print("Reversed number is:", rev)


# -----------------------------
# First 10 Fibonacci numbers
# -----------------------------
a, b = 0, 1
count = 0

while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

print()


# -----------------------------
# 5x5 Star Pattern
# -----------------------------
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# -----------------------------
# Triangle Pattern
# -----------------------------
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# -----------------------------
# Reverse Triangle
# -----------------------------
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# -----------------------------
# Number Triangle
# -----------------------------
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# -----------------------------
# Stop when divisible by 7
# -----------------------------
for i in range(1, 20):
    if i % 7 == 0:
        break
    print(i)


# -----------------------------
# Print even numbers
# -----------------------------
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)


# -----------------------------
# Print odd numbers
# -----------------------------
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


# -----------------------------
# for-else example
# -----------------------------
for j in range(1, 20):
    print(j)
else:
    print("Loop is completed")

# -----------------------------
# check the palindrome strings
# -----------------------------

s = input("enter the str: ")
if s == s[::-1]: # means str slicing means starts from end, moves backword, takes all the charactors
    print("palindrum")
else:
    print("it's not an palindrum ")


# -----------------------------
# check the patterns 
# -----------------------------

rows = 5 
for i in range (1,rows+1):
    print(" "* (rows-1)+"*"*(2*i))



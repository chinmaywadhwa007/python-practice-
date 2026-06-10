# if else use for the decision making
# it helps the program to make a condition on the bases of what user want

age = 18
if age >= 18:
    print("you can vote")
else:
    print("you can't vote")


# example 2nd with the numbers
number = 10
if number >= 0:
    print("number is positive")
else:
    print("negative number ")


# understanding the conditions
# check if the condition is true or false
# 5 > 2      # True
# 10 == 5    # False
# 7 != 3     # True

e = 9
if e % 2 == 0:
    print("even")
else:
    print("odd")


# check if weather a year leap or not
year = 2000
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("it's an leap year")
else:
    print("its not an leap year ")


# find the gretest of the three numbers
a, b, c = 12, 89, 34
if a > b and a > c:
    print("a is gretest")
elif b > c:
    print("b is gretest")
else:
    print("c is gretest")


#  check if the number is divisible by 5
num = int(input("enter the value: "))
if num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# check if the charactor is a vowel

ch = "r"
if ch in ("aeouAEIOU"):
    print("this is an vowel ")
else:
    print("the charactor is consonent ")


# check if a number is in range 1-100
hub = 45
if 1 <= hub <= 100:
    print("its in the range ")
else:
    print(" not in the range ")

# check  if number is multiple by 3 or 5
value = int(input("enter the value for checking multiple o 3 and 5: "))
if value % 3 == 0 and value % 5 == 0:
    print("number is divisible by 3 and 5")
else:
    print("its not divisible by 3 and 5  ")


# side1=int(input("enter the first side of the triangle"))
# side2=int(input("enter the second side of the triangle"))
# side3=int(input("enter the third side of the triangle"))

# if side1==side2 or side2==side3 or side3==side1:
#     print("equal")
# elif side1==side2 or side2==side3 or side3 ==side1:
#     print("isoc.")

# else:
#     print("scalen")

# login page of the user and the admin
# correct_username = "chinmaywadhwa0012 "
# correct_passcode = "chinmaywadhwa001 "
# username = input("enter your name: ")
# passcode = input("enter your passcode: ")
# if username == correct_username and passcode == correct_passcode:
#     print("login pass u can in ")
# else:
#     print("you are not allowed to logged in ")

marks = 55;
if marks>=90:
    print("A+")
elif marks>=75:
    print("B+")
elif marks>=60:
    print("B")
elif marks>=40:
    print("C")
else:
    grade ="fail"
    print("Grade: ",grade)


# function in the python  a function is a block of code whic only runs when it called
# creating functions
# this is the syntax of the function and how we call it
def function():
    print("hello world")


function()

# -------- example 2------


def my_function():
    print("loggedin successfully!!")


my_function()
my_function()
my_function()

# ------- example 3 --------


def name_function(name):
    print("hello "+name)


name_function("chinmay")
name_function("virat")
name_function("rohit")

# example 3 with full names

# in this we can use the multiply paras in function


def my_function(fname, lname):
    print(fname + "  " + lname)


my_function("rohit",  "singh")


# arbitrary arguments ,*args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# stores data in the form of tuple

def hello(*fruits):  # its just another way of finding the index of tuple or any function
    print("there are diff type's of fruits in the diff season..!"+fruits[5])


hello("mango", "orange", "apple", "litchi", "watermelon",
      "banana", "melon", "hfkjehf", "fewgjfgwj", "wfwief")


# keyword arguments
# you can also send the arguments with keys = value syntax
def function(child1, child2, child3):
    print("the youngest child among these is : " + child3)


function(child1="chinmay", child2="vikas", child3="rohan")


# now we will see the diff method called kwargs donated by **

# arbitrary method called kwargs
def kwargs(**kid):  # this method is called mix up of the key and value...
    print("his first name is "+kid["lastname"] + " " + kid["fname"])


kwargs(fname="chinmay", lastname=" wadhwa", name="hello")


# default parameter values
def default(country="india"):
    print(" i am from :"+country)


default("canada")
default("germany")
default()
default("aussess")


# passing the list from the arguments
def print_vegitables(vegges):
    for i in vegges:
        print(i)


a = ["carrot", "broccali ", "spinich"]
print_vegitables(a)

# return values from the functions


def my_function(x, y):
    return x+y


print(my_function(2, 3))
print(my_function(3, 7))
my_function(3, 7)

# you can specify that a function can have only positional arguments or keyword arguments
# to specify that a functions can have only positional  args,add, / after the args
# positional only arguments

# “Arguments before / can ONLY be passed by position.”


def function(x, /):
    print(x)
# Why use / ?
# It is useful when:
# You want arguments to depend only on order
# You don’t want users changing parameter names
# Built-in Python functions often use this

# So / is useful for:

# cleaner APIs
# avoiding accidental keyword usage
# protecting internal parameter names
# reducing future bugs/errors


function(33)


# keyword only arguments
def fun(*, x):
    print(x)


fun(x=3)

# --- example 2 ---


def hello(*, x):
    print(x)


hello(x=232323)


# combine positinal-only and the keyword-only
# note when we use "/" this keyword means everything before / is an positinal only so we have to use "," after every keyword
# not2 and when we use the "*" this keyword we have to use the "x=7"
def my_function(a, b, /, *, c, d):
    print(a+b+c+d)


my_function(5, 6, d=7, c=8)


# recursion method in python
# A function calling itself again and again until a stopping condition is met.
def recursion(i):

    if i == 1:
        return 1
    else:
        return i + recursion(i-1)


print(recursion(10))

# example 2 in recurson method with the single line of code


def avoid(n):
    return "even" if n % 2 == 0 else "odd"


print(avoid(34))

# example 3 with the factorial method


def factorial(h):
    if h == 0 or h == 1:
        return 1
    return h*factorial(h-1)


print(factorial(6))

# example 4


def max_of(a, b, c, d):
    return max(a, b, c, d)


print(max_of(45, 21, 24, 75))


# lambda function
def add_lambda(x, y, z): return x+y+z


print(add_lambda(5, 4,  6))


# sqaure of lambda
def square(x): return x**2


print(square(45))
print(square(100))


# example
# in this we have to convert the celsius into fahrenheit using map()and list and lambda
# A lambda is a short anonymous function.
# map() applies the function to every item in the list. 
#why it only works with list 
#map() returns a map object.
# To see actual values, we convert it into a list:
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (9/5)*c+32, celsius))
print(fahrenheit)

for i in range(3):
    print(fahrenheit[i])

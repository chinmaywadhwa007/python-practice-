#this is where we define the function 
def fun():
    print("hello world")
fun()

# default argument 
def hello(x,y=30):
    print("x:",x)
    print("y:",y)

hello(30)

# keyword function  
def student (name,surname):
    print(name,surname)
student(name='chinmay',surname='wadhwa')
student(surname='chinmay',name='wadhwa') #it will reverse the function 

# argument python....
#*args: collects extra positional (non-keyword) arguments as a tuple.
def funs(*args):
    return sum(args)

print (funs(1,5,10))

# **kwargs: collects extra keyword arguments as a dictionary.
def funs(**kwargs):
    for k, val in kwargs.items():
      print(k, val)

funs(a=1, b=5, c=10)
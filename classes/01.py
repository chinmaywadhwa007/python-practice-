# class is like a blueprint for creating an object
# it defines attributes (variables) and methods (functions) that describes an obj
# an obj is an instance of a class
# when we create an obj pythons allocates memmory and stores its arttributes

class hello():
    x = 5
    y = 10


obj = hello()
print(obj.x)
print(obj.y)


# use the constructor (__init__)
# constructor runs autmatically when object is created
class hey():
    # self means current object python automatically sends the obj iteself
    def __init__(self, a):
        self.x = a


obj1 = hey(10)
print(obj.x)

obj2 = hey(45)
print(obj2.x)


# use the method _str__() method
# the__str__()method controls what should be returned when the class obj is represented as a strings
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


p1 = person("chinmay wadhwa", 24)
p2 = person("user", 45)
p3 = person("user2", 18)
print(p1, p2, p3)


# multiply obj with diff values
class hello():
    def __init__(self, value):
        self.x = value


obj01 = hello(55)
obj02 = hello(5454500)
print(obj01.x)
print(obj02.x)


# add a method

class names():
    def __init__(Self, name):
        Self.name = name

    def wewew(self):
        print("hello world", self.name)


obj = names("chinmay wadhwa")
obj.wewew()


# updating attributes using the method
class method():
    def __init__(self, value):
        self.x = value

    def update(self, new_value):
        self.x = new_value


obj = method(45)
print("before =", obj.x)
obj.update(100)
print("after =", obj.x)


# class with default values

class stud:
    def __init__(self, name="unknown", roll=0):
        self.name = name
        self.roll = roll


s1 = stud("rohan", 45)
s2 = stud()
print(s1.name, s1.roll)
print(s2.name, s2.roll)


# classes with the multiple methods
class calci:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3


obj = calci(4)
print("sqaure of the number: ", obj.square())
print("cube of the number: ", obj.cube())

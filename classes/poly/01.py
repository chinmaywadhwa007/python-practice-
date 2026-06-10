# here we starts the polymorphism in the oops in python
# this means "many forms"
# in programming it allows the same function or operator to behave differntly depanding on the obj it is acting upon


# polymorphism with the method overriding

class animal:
    def sound(self):
        return "some generic sound wispers!!"


class dog(animal):
    def sound(self):
        return ("barks ")


class cat(animal):
    def sound(self):
        return ("meow!!")


animals = [dog(), cat(), animal()]

for a in animals:
    print(a.sound())


# polymorphism with functions
class car:
    def weeels(self):
        return "car has four wheels"


class bike:
    def weeels(self):
        return "bike has 2 wheels"


def displaywheel(vehicles):
    print(vehicles.weeels())


# polymorphism
c = car()  # it created working with the functions
b = bike()
displaywheel(c)
displaywheel(b)


# lets understand the scope now in variable
# means from where we decleared the variables in python

# there are mainly its two types 1. local and 2nd is global
# local scopes a variable that can created only inside any functions


def myfunction():
    x = 100  # this is local scope
    print(x)


myfunction()


# 2nd in global scope
x = 10000000


def any():
    print(x)


any()

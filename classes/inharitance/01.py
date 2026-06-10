# innharitance is one of the most important topic of the oops in python

# it allows one class to reuse porperties and method of another class

# basic syntax

# It helps in code reusability and extending features.

class parent:
    pass

# child class  gets everything from the parents


class child(parent):
    pass


# example 1

class animal:
    def eat(Self):
        print("animal is eating")


class dog(animal):
    def barking(self):
        print("dogs barked at the store...!")
# what happens dog class does not have eat()
# python search inside dogs and then inside animal "it finds the method in animal"


d1 = dog()
d1.eat()
d1.barking()

# example 2


class parent:
    def show_parent(self):
        print("this is the parent class")
# child class inharitance from parent


class Child(parent):
    def show_child(self):
        print("this is the child classs")


# create object of child()
obj = Child()
obj.show_parent()  # inherited form parent
obj.show_child()  # from child

# constructor in inharitance


class parent:
    def __init__(self, name):
        self.name = name


class child(parent):
    def __init__(self, name, age):
        # why we use the super()
        # because we want to call the parent class constructor (__init__)
        # and we want cleaner and maintainable code
        super().__init__(name)  # this will call from parent class
        self.age = age

    def display(self):
        print(f"name:{self.name},age:{self.age}")


c = child("chinmay wadhwa ", 45)
c.display()


# when we have multiply inharitance
class Father:
    def skilled(Self):
        print("father: gardening, programming, sleeping")


class mother:
    def skilled(self):
        print("mother:cooking, painting")


class child(mother, Father):
    def skilled(Self):
        print("child: biker and traveller")
        Father().skilled()
        mother().skilled()


ooo = child()
ooo.skilled()


# multilevel inharitance
class cricket():
    def skills(self):
        print("virat is an good batsman")


class football():
    def hello(self):
        print("messi is an good footbooler")


class hello(cricket, football):
    def how(self):
        print("rohit  is an good batsman")


sport = hello()
sport.skills()
sport.hello()
sport.how()

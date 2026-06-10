# inharitance class
# inharitance allows a child/derived to  use the properties and the methods of another class (parent/base)
# it help to become resuability and extending feature...


# parent class
class parent:
    def show_parent(self):
        print("this is the parent class..")


class child (parent):
    def show_child(self):
        print("this is the child class")


obj = child()
obj.show_parent()
obj.show_child()

# construtor in inharitance


class parent():
    def __init__(self, name):
        self.name = name


class child(parent):
    def __init__(self, name, age):
        # why we use the super because to call the parent class
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"name:{self.name},{self.age}")


c = child("chinmay wadhwa", 45)
c.display()

# types of inharitancce
# single inharitance


class animal:
    def sound(Self):
        print("animal makes sound")


class dog(animal):
    def sound(Self):
        super().sound()
        print("dogs barks ")


d = dog()
d.sound()


# multiple inharitance
class father:
    def skill(self):
        print("father : working , gardening , programming")


class mother:
    def skill(self):
        print("mother : cooking,social worker,painting")


class child(father, mother):
    def skill(self):
        print("child:sports")
        father().skill()
        mother().skill()


skill = child()
skill.skill()


# multilevel inharitance
class grandparent:
    def show1(self):
        print("i am grandparent")


class parent(grandparent):
    def show2(Self):
        print("i am parent")


class child(parent):
    def show3(self):
        print("i am child of my grandparent and parent")


c = child()
c.show1()
c.show2()
c.show3()

# Hierarchical Inheritance
# In Hierarchical Inheritance, one parent class is inherited by multiple child classes
# Parent class


class parent ():
    def property(self):
        print("house and car")

    # child class 1


class son(parent):
    def job(Self):
        print("son has the job")

    # child class 2


class daughter(parent):
    def business(parent):
        print("daughter has a business")


# create an obj
s = son()
d = daughter()
s.job()
d.business()


# method overriding
# child class redefines a parent method

class parent:
    def greet(self):
        print("hello from parents side ")


class child(parent):

    def greet(self):  # overriding
        print("hello from child")


obj = child()
obj.greet()


# a class become an iterator if it implements two methods
# __iter__(self) → returns the iterator object itself.

# __next__(self) → returns the next value. If there are no more values, it should raise StopIteration.

class countDown:
    def __init__(self, start):  # willl start from this
        self.current = start

    def __iter__(self):  # then goto this
        return self  # the iterator obj return itself

    def __next__(self):  # then it matches the condtion using conditinal statement
        if self.current >= 30:
            raise StopIteration  # Terminates iteration
        else:
            #  +=1 for increasing the order for the range starting from the 11
            self.current += 1  # self.current=self.current+1
            return self.current


# using the ieterator
cd = countDown(10)  # countdown starts from here till 30
for num in cd:
    print(num)

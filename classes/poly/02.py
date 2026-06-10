# class method in python or we can say that decorative method in the python

class parents:
    count = 0

    def __init__(self, name):
        self.name = name
        parents.count += 1

    @classmethod
    def get_counted(hello):
        return hello.count


p = parents("a")
p2 = parents("b")
p3 = parents("c")
print(parents.get_counted())

# now we will study the static method


class math:
    def add(a, b):
        return a+b


print(math.add(4, 6))


class animal:
    def sound(self):
        print("animal makes a sound")


class dog(animal):
    def sound(self):
        super().sound()
        print("dogs barks ")


d = dog()
d.sound()

# using super() in a single  inharitance


class parant:
    def __init__(self, name):
        self.name = name


class child(parant):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


c = child("chinmay", 4500)
print(c.name, c.age)


# using super() in overiding

class a:
    def show(self):
        print("class a")


class b(a):
    def show(self):
        super().show()
        print("class b")


b = b()
b.show()

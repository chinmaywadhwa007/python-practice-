# **kwargs allows a function to accept multiple keyword arguments
# Python stores these keyword arguments inside a dictionary
def user(**kwargs):
    print(kwargs)


user(name="chinnmay", lastname="wadhwa")


# we can use the both at the same time

def demo(*args, **kwargs):
    print(args)
    print(kwargs)

# we can build this together but the output will comes seprated
# so 1,2,3 will become tuple
# and name age will become dictnory 
demo(1, 2, 3, name="chinmay wadhwa ", age=24)



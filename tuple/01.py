# A tuple is one of Python's four built-in data types used to store collections of items.
# It is ordered, immutable (unchangeable), and allows duplicate values.

#tuple  defination explanation

my_tuple=("apple","mango","orange")
print(my_tuple)

tuple= ("apple",) # with this is we call the tuple via type
print(type(tuple))

#access the elementt in the tuple 
fruits = ("orange","apple","black_current")
print(fruits[1])
print(fruits[-1])
print(fruits[0:2])

# how to  check the tuple length in py
this = ["mohali","jaipur","kashimir"]
print(len(this))

#how connstructor works in the tuple
# hello = tuple(("apple", "banana", "cherry")) 
# print(hello)

#access the tuple item 
this_tuple=["hello","world","python"]
print(this_tuple[0])

#negative indexing 
thistuple = ("apple", "banana", "cherry")
print(thistuple[-2])

#return the third fourth and the 5th element

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#check if the item is ready or not 
L=("apple", "banana", "cherry")
if "virat" in L:
    print("yes","this item is exist in the tuple")


#update the tuple 
#changes the tuple
#once a tuple is created you cannot change  its value tuples are unchangeable ,or immutable as it also called

x=("apple","banana","orange")
y=list(x)
print(y)

y[1]="kiwi"
x=tuple(y)
print(x)


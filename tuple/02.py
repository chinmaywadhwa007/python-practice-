x = ("apple", "banana", "cherry")
y = list(x)    
print(y)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y   #thistuple=thistuple+y
print(thistuple)

#remove the item 
#in this we will remove the item from the tuple  
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
print(y)
y.remove("cherry")
thistuple = tuple(y)
print(thistuple)

#the del keyword can delete the tuple completely
h = ("apple","orange","lemon")
del h # this will delete the entire tuple 
# print(h)

#unpacking a tuple
hellos = ("hello","world",("python"))
(green,yellow,blue)= hellos
print(green)
print(yellow)
print(blue)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green,*a,yellow,red) = fruits
print(green)
print(a)

# joining the two tuple 
tuple1 = ("1","2","3","4","5")
tuple2 = (1, 2, 3)
tuple3=tuple2+tuple1
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
a = fruits * 10
print(a)
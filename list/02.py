
#using appand () adds at the last 
appand = ["apple","mango", "orange"]
appand.append("kiwi")
print(appand)

#insert 
insert = ["apple","mango", "orange"]
insert.insert(2,"orange")
print(insert)

#extand method or the merge method 

method = ["apple","mango", "orange"]
method2=["amazon","microsoft","google"]
method.extend(method2)
print(method)


# remove list items : the remove() method is to remove the item from the list 

thislist = ["amazon","microsoft","google"]
thislist.remove("google")
print(thislist)

# remove Specified Index
#this method is called the pop method removes the index you want 

hello = ["amazon","microsoft","google"]
hello.pop(0)
print(hello)

# if u don't give the value number to pop method it will remove the last value of  the list 
list= ["amazon","microsoft","google"]
list.pop()
print(list)

# the delete keyword can also remove the value in the list 
delete = ["jaipur","mumbai","somnath"]
del delete[0]
print(delete)

# if u want to delete all the list of the list it will remove all the element 

# u =["jaipur","mumbai","somnath"]
# del u # this will remove the whole list  
# print(u) 

# if u want to vanish the list and the [] only this will remain the last thing 
clearm=["jaipur","mumbai","somnath"]
clearm.clear()
print(clearm)

# sorting the list 
list1 = [100,10,20,30,40,100]
list1.sort() # this will go to small to to  bigger number 
print(list1)

# sort desending 
# to use sort desending use the keyword argument reverse =true 
fruit=["orange ","mango","apple","watermelon","kiwi"]
fruit.sort(reverse=True)
print(fruit)


#use of the copy method 
thislist=["orange ","mango","apple","watermelon","kiwi"] #this will copy the exact same value to the  other variable
# a=thislist.copy()
# print(a)

#use the list method
#another way to making the copy  of the list 

py = ["apple", "banana", "cherry"]
# mylist = list(py)
# print(mylist)

#use of the slice operator 
#u can also make a copy by using the slice() oprator
hislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# join the list means two list in the same list is called join method 

suppose = ["l1","L2","L3"]
suppose2= ["L4","L5","L6"]
suppose.extend(suppose2)
print(suppose)

#rotate the list
lst =["1","2","3","4","5"]
O = 12
O=O%len(lst)
print(lst[-O:]+lst[:O])

#asking user to rotate the input 
lst =["1","2","3","4","5"]
O = 12
O =int(input("enter your rotation number: ") )
O=O%len(lst)
print(lst[-O:]+lst[:O])
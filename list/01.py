#what do u mean by list in python
#ordered (elements have a specific postions )
#mutable (can c=be changed after creation )
#allows duplicates 
# can hold mixed datatype(int,string,float,even,other list ) this is called the list in the python 

chinmay = [10,20,30,40]
print(chinmay)  

fruits = ["apple","mango","orange","cherry"]
number =[1,2,3,4,5]
# we can print any number string float even anything in the list in python
mixed = ["hello",5,25,2.5, True]
empty=[]
print(fruits)
print(number)
print(mixed)

thislist= ["apple","banana","cherry","mango","kiwi","papaya","orange "]
#with ths we can find the length of the list 
print(len(thislist))

#we can check the type()
mylist = ["apple","banana","cherry"]
print(type(mylist))

#the list construtor how construtor works in the python

hello_list = list(("apple","orange","mango"))
print(hello_list)
print(type(hello_list))

#access item 
how = ["virat","rohit","dhoni"]
# by using this method we can access the item in the list 
print(how[0])

#negative indexing 
negative = ["virat","rohit","dhoni"]
print(negative[-1])

#range of the list how we can find the range of the list 

range = ["apple","orange","mango","Rcb","csk","gt","mi"]
# means we can print from the range of rcb to mi in the situation
print(range[3:])
range = ["apple","orange","mango","Rcb","csk","gt","mi"]
# means we can print from the range of apple to rcb  in the situation
print(range[:4])
range = ["apple","orange","mango","Rcb","csk","gt","mi"]
# means we can print from the range of "orange" "mango" "rcb" "csk" "gt"  in the situation
print(range[-6:-1])

#check the list if the item exist or not 
check = [ 10,20,30,40,50]
#check if 40 exist in the list or not 
#by this  way we can check rather the number is there or nor 
if 45 in check:
    print("item found!!")
else:
    print("item not found ")


# next we will  see how we can change the item from the list or not 

lists = ["apple","orange","yellow"]
lists[1]="blue" # here we can change from orange to blue 
lists[2]="black" # here we can change from yellow to black 
print(lists)

#change the range between the numbers in the list 

replace= ["a","b","c","d"]
replace[1:3]=["A"]
print(replace)


# replace two items with the more items 

replace_0=["a","b","c","d"]
replace_0[1:3] = ["x","y","z"]
print(replace_0)



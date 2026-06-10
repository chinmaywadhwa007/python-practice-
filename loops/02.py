# practice question for the python
# print from  1  to 10
# by this we will know the range between 1 to 11
for i in range(1, 11):
    print(i)

    # print even number between tha range of 1 to 11

# for a in range(2, 51, 2):
    # print(a, end=" ")

# print the characters in a string "pythonloops"
text = "pythonloops"
for x in text:
    print(x, end=" ")

# print square of numbers from 1 to 10
for w in range(1, 11):
    print(w**2)

# iterate through a list (10,20,30,40)
list = [10, 20, 30, 40]
for v in list:
    print(v)


# sum of all element in the list
hello = [10, 20, 30, 40]
total = 0
for num in hello:
    total += num
    print("sum", total)


# multiplication table of a number
n = int(input("enter the number : "))
for I in range(1, 11):
    print(f"{n} x {I} = {n*I}")


# iterate through dictinory
# we can use this for to create object using loops 
d = {'name': 'alice', 'age': '23'}
for A in d:
    print(A, ":", d[A])

    #print element from tuple
    t = (1,2,3,4,5)
    for  Q in t:
         print(Q,end="")

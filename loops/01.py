# python loop
# python has two primitive loops commonds
# while and for  loop

# the while loop
i = 2
while i <= 50:
    # print(i)
    i = i+2
# this will be the break statement
j = 3
while j <= 10:
    # print(j)
    j = j+3
    if j == 9:
        break

# this will be the continue statement
c = 6
while c <= 10:
    c += 10
    if c == 5:
        continue
    # print(c)

# the else statement
h = 1
while h < 6:
    # print(h)
    h += 1
# else:
#     print("h is no smaller  less than  6 ")


# is time for the for loop how it works
helo = ["apple", "banana", "mango"]
for y in helo:
    print(y)

# looping through a string
# for x in "banana":
#     # print(x)

# the break statement
fruits = ["apple", "orange", "graps"]
for xl in fruits:
    print(xl)
    if xl == "orange":
        break


# continue statement
OLA = ["hello", "world", "from", "python"]
for g in OLA:
    if g == "from":  # this will be skip and the other will continue
        continue
    print(g)

# the range ()function
for gh in range(5):  # this wull print the value until the range hits
    print(gh)
# just an example for the range ()function
for ht in range(10, 51):
    print(ht)


# nested loops
# nested = ["hello", "world", "python"]
# welcome = ["welcome", "user ", "to ", "the", "coding", "world"]
# for u in nested:
#     for d in welcome:
#         print(u, d)


# the pass statement 
for f in["10","20","30"]:
    pass


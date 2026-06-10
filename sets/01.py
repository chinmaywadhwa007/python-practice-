# here we will see how sets work in the pyhton

# sets means a collection of unique value that means
# no dulpicates items are allowed,item are unordered,setes are mutable (you can add/remove items )

# syntax of the setes should use {} peranthises bracket
# it will remove the duplicate number and show only one in terms of multiply
number = {1, 2, 3, 4, 4, 4, 5, 6}
print(number)


# suppose user  login in to app
logged_users = set()
logged_users.add("chinmay wadhwa")
logged_users.add("rahul")
logged_users.add("chinmay wadhwa")  # we can't login same user multiple times
logged_users.add("virat")
print(logged_users)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", 1, True, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", 0, False, True}
print(thisset)

# gets the length of the set
myset = {"apple", "orange", "mango"}
print(len(myset))
# what will be the type of the set  as follow
type_set = {"hello", "world", "set", "in", "python"}
print(type(type_set))

# we can use the set as the operator also
# this will convert list in to the set
ops = set(("london", "nyc", "goa", "delhi"))
print(ops)
# check if the element exists in the set or not
# if yes it will print boolian true
ops = set(("london", "nyc", "goa", "delhi"))
print("london" in ops)
# check if is not there
ops = set(("london", "nyc", "goa", "delhi"))
print("virat" not in ops)

# we can add the items in the  sets tooo
# note set is unordered so it can came anywhere in the set
add = {"apple", "banana", "cherry"}
add.add("orange")
print(add)

# to marge to set in the one

marge_set = {"1", "2", "3", "4"}
sets = {"5", "6", "7"}
marge_set.update(sets)
print(marge_set)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove the item from the set
removeIt = {"apple", "banana", "cherry"}
removeIt.remove("apple")
print(removeIt)

# remove the random item in the set

ji = {"k", "v", "d", "e"}  # it will remove the item randomly...
ji.pop()
print(ji)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# another method to join the set
see1 = {"hello", "world"}
see = {"1", "2", "3", "4"}
see2 = see1.union(see)  # but fill it randomly...!
print(see2)

# interection
# this will only print the common element in the diff set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# but if we have to do it in the same set we can do by using this
combine_1 = {"apple", "google", "samsung"}
combine_2 = {"apple", "google"}
combine_1.intersection(combine_2)
print(combine_1)

# we have the diff form of interction called &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

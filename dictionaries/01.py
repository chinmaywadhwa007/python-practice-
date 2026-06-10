#now lets start the dictinories  are used to store data calues in key: value pairs
dis ={
    "name":"chinmaywadhwa",
    "age":"23",
    "email":"chinmaywadhwa01@gmail.com",
    "passward":"chinmaywadhwa01@",
}
print(dis)

#in dict items are changed, ordered, and do not allow duplicates 

user_Date={
"name":"chinmay wadhwa ",
"name":"rahul unknown",# in this the latest one will be print older one will not print 
"email":"abc@gmail.com",
"pass":"hello world from object of python",
}
print(user_Date)

# we can check the length of the object in the python
dis ={
    "name":"chinmaywadhwa",
    "age":"23",
    "email":"chinmaywadhwa01@gmail.com",
    "passward":"chinmaywadhwa01@",
}
print(len(dis))


# dictinory items - datatypes

unknown_data={
    "user":"unkown01",
    "age":"23",
    "year":"2025",
    "colors":["black","blue","yellow"]
}
print(unknown_data)
#we can check the tyoe of the dict
unknown_data={
    "user":"unkown01",
    "age":"23",
    "year":"2025",
    "colors":["black","blue","yellow"]
}
print(type(unknown_data))

#we can use dict with the constructor 
user_input=dict(name="chinmay",age="24",year="2003")
print(user_input) 
#if we have to accessing the items in the dict
# this will help me to access the element in the dict
unknown_data={
    "user":"unkown01",
    "age":"23",
    "year":"2025",
    "colors":["black","blue","yellow"]
}
x=unknown_data["age"]
print(x)

#accessing the items 

this = {
    "brand":"royel enfield",
    "year":"1964",
    "model":"meteor 350",
}
y = this.get("brand")
print(y)

#if we have to access keys in the dict
data = {
    "brand":"royel enfield",
    "year":"2000",
    "model":"hunter 350",
}
d = data.keys()
print(d)

# this method will gives the value how many values are there in the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.values())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
} 
x = car.values()  
print(x) #before the change
car["year"] = 2020 #this will update the latest one....
print(x) #after the change

#we can add keys also in this 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

# The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()# with this will return the tuple method in the dict...
print(x)
# if we have to check the key and value present or not 
hello={
    "brand":"woksvogon",
    "model":"polo",
    "year":"2024",
} 
if "model" in hello:
    print("yes this key/value present in the hello dict...")

    #we can change the value also of the keys 

change={
    "user":"hello world",
    "course":"python basics ",
    "purchase plan":"20000",
}
change["user"]="chinmay wadhwa"
print(change)

# we can remove the item using pop method
change={
    "user":"hello world",
    "course":"python basics ",
    "purchase plan":"20000",
} #in this we have to give the value to the pop that method can delete what we have to delete 
change.pop
print(change)
change={
    "user":"hello world",
    "course":"python basics ",
    "purchase plan":"20000",
} #in this we have to give the value to the pop that method can delete what we have to delete 
change.popitem()
print(change)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
del thisdict["model"]
del thisdict["year"]
print(thisdict)# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
del thisdict["model"]
del thisdict["year"]
print(thisdict)


# The clear() method empties the dictionary:
clear = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
clear.clear()
print(clear)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)



# access
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(len(myfamily))
print(myfamily["child2"]["year"])


zeetron={
    "students":{
        "chetan":{
            "skills":{
                "python":5,
                "ml":3,
                "excel":8
            }
        },

         "akshay":{
            "skills":{
                "python":6,
                "ml":0,
                "excel":5
            }
        }
        
    }
    
}

print(zeetron["students"]["akshay"]["skills"]["ml"])
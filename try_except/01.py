# here we use the two statement too run the code it just like the try and catch method in the node js
try:
    print("x")
except:
    print("error occured ")

# with  the help of  the global variables
x = "hello  world "
try:
    print("x")
except:
    print("error wll come ")

try:
    hiuihu = henwihewhr
    print(hiuihu)
except:
    print("error will come")

# we use another keyword called finally

try:
    print("wd")  # if this wrote correctly then output will be try and finally if it doesn't then the output will be the  except and th e finally
except:
    print("something went wrong")
finally:
    print("khel khtm ")


try:
    num = int(input("enter a nnumber :-"))
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("can not divisble by zero ")
except ValueError:
    print("wrong i/p given ")

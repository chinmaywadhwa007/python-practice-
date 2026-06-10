#will see how conditinal statement works here
year = 2024
if(year%4==0 and year % 100 !=0) or (year % 400 == 0):
    print("leap year")
else:
    print ("it's not an leap year")

#find the  greatest of three number 
a,b,c =12,45,5
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greatest")


# check if a  character is  a vowel
#in mmeans it checks the membership inside the aeiouAEIOU
ch = 'f'
if ch in 'aeiouAEIOU':
    print("vowel")
else:
    print("consonent") 


# check the number in the range or not 
num = -89;
if 1<=num <=100:
    print("in range")
else:
    print("out of the range")


nums = 25
if nums % 3 == 0 and nums % 5 == 0:
    print("multiple of 3 and 5 ")
else:
    print("not the multiple of 3 and 5")



# login page hoow it works 

correct_name = "chinmay"
correct_pass = "123456789"
username= input("enter your name: ")
password= input("enter your pass: ")
if username==correct_name and password==correct_pass:
    print("login succesfull")
else:
    print("invalid credentials please enter correct one's")



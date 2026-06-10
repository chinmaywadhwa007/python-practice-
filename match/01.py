lang = input("enter the lang:")

match lang:
    case "english":
        print("hello! how are u ")
    case "spanish":
        print("hola! how are u ")
    case "franch":
        print("bonjour! how are u ")
    case "hindi":
        print("namste ! app kaise hai ")
    case _:
        print("no match found here ")


days = int(input("enter your day here:"))
match days:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("no days found")

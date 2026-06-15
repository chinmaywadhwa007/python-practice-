from functools import wraps

#this is the original function where all this started 
def loggedIn(user):
    @wraps(user)
    #by this we created aother function with args without knowing the params 
    def wrapper(*args, **kwargs):
        print(f"calling:{user.__name__}")
         # Execute the original function
        result = user(*args, **kwargs)
        print(f"finished loggedin :{user.__name__}")

        return result
     # Execute the original function
    return wrapper


@loggedIn
def signedup(users):
    print(f"user signed up successfully: {users} hello")


signedup("welcome back chinmay wadhwa ")

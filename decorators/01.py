from functools import wraps


def my_decorator(func):
    @wraps(func)
    # this is called the nested function because it defined it in the parent def
    def wrapper():
        print("before function runs ")
        func()
        print("after function runs ")
    return wrapper

# decorators means its a special type of def which let u add functinality to a function without modifying it original code


@my_decorator
def great():
    print("hello from decorators @")


great()
print(great.__name__)  # because it returning with the wrapper part

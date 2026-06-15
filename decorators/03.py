from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(User_Role):
        if User_Role != admin:
            print(
                "you have to be admin for inrolled in this page other vise in 5 s i while logged out u ")
        else:
            return func(User_Role)

@require_admin
def acess_tea_inventory(role):
    print("access granted as user passed ")


acess_tea_inventory("role")
acess_tea_inventory("admin")

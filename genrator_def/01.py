def chai_shell():
    try:
        while True:
            #The generator produces values one at a time instead of creating the entire list at once.
            order = yield "waiting for an order for chai "
    except:
        print("stall closed , u have to wait for to open it ")


stall = chai_shell()
print(next(stall))
stall.close()

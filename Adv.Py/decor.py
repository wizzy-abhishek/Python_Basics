def decorator(func):
    print("Main func")
    def wrapper():
        print("1st line ")
        for i in range(2):
            func()
        print("Inner last line")
    return wrapper


@decorator
def shout():
    print("HELP")

shout()
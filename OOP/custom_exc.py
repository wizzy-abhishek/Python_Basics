class Error(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class AgeException(Error):
    def __init__(self, *args):
        super().__init__(*args)

age = int(input("Enter you age\n"))

try:
    if age < 18:
        raise AgeException("You are a minor")
    else:
        print("Welcome to the Flight")
except AgeException as ex:
    print(ex)
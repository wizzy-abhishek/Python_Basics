try:
    a = 19/0
except NameError or ValueError or ZeroDivisionError as ex: 
    """
        This doesn't works here in python, here we are not getting any syntax error.
        However, the interpreter will only handle the first case of exception written.
    """
    print(ex)
else:
    print("Try block executed succesfully")
finally:
    print("The code ends here") 
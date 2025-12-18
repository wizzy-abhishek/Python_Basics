try:
    a = 19/0
except NameError or ValueError or ZeroDivisionError as ex:
    print(ex)
else:
    print("Try block executed succesfully")
finally:
    print("The code ends here")
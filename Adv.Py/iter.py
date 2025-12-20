my_list = [1,0.2,1111,'Abhishek']

iterator = iter(my_list)

try:
    for i in iterator:
        print(i)
        val = next(iterator)
        print(f"using next: {val}")
except StopIteration as ex:
    print(ex)
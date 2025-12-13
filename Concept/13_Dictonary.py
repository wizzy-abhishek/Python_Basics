empty_dict = {}
print(type(empty_dict))

marks = {
    "Abhishek" : 6 ,
    "Gargi":84 ,
    "Abhishek":12 # Value of Abhishek got replaced by 12 
} 

# Traverse fast than list
" It is unorder , mutable and indexed " 
" It cant have duplicate keys "

print(marks , type(marks))

print(marks.items())

keys = marks.keys()
print(keys)

abhishek = marks["Abhishek"] # If key is not present then it will throw an error

print(abhishek)

marks.update({"Gargi":6 , "Anand":84})
print(marks)

print(marks.get("Abhishek Anand")) # This returns none id not present

# marks.clear()

marks.pop("Abhishek")
marks.popitem()

print(marks)
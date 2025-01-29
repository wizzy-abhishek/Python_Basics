t = (1 , True , "Abhishek" , "Anand" , 1)

# If we dont include , 
# after declaring only one element it wil treat it as int

print(type(t))

print(t)
print(t[0])

#t[2] = 1234 Immutable so cant 

repeat = t.count(1)
print(repeat)

i = t.index(1)
print(i)

length = len(t)
print(length)

# Here if we slice a new tuple will be returend

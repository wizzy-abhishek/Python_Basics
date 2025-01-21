a = " Abhishek "
b = 'abhishek anand'
c = '''Abhishek'''

#slice

sliced_name = a[0:4] # 4 Excluded
slice_name = a[-4:]

print(sliced_name)
print(slice_name)

# Slicling with skip value

num = '123456789'

num_slice = num[1:7:3] # Third digit after 1 till 7

print(num_slice)

# String functions 

length = len(a)
print(c.endswith("shek"))
print(c.startswith("abhi"))
print(b.capitalize())
print(a.strip())
print(a.upper())
print(a.replace("Anand" , "Hello"))
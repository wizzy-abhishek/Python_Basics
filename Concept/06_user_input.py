a = input("Enter any number "); # we can wrap here too
b = input("Enter any number ")

c = a + b ; # This will also concate it cause it take input as STRING 

# print(a+b) This considers it as String

print(c);

a = int(a); # If we entered a float it will thr invalid literal so we have to use TRY CATCH block 
b = float(b);

print(a+b);
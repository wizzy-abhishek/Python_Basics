set1 = {1,2,3,5,4,4, "Abhishek"}

# Unordered , unindexed , no way to change items , no duplicate values 

e = set() # empty set 
set1.add("Gargi")

print(set1 , type(set1))

# set1.clear()
set1.remove(4)
set1.pop()

print(set1)

print(len(set1))


#set union and intersection

s1 = {1,2,3}
s2 = {84,1,6}

print(s1.union(s2))

print(s1.intersection(s2))
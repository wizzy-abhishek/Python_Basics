friends = ["Hello" , "Abhishek" , 12345 , True , 12.5]

print(type(friends))

#Unlike string list are mutable 

friends[0] = "Heyyy"
#friends.sort()
friends.reverse()
friends.insert(4 , "Aur be=")
friends.pop(0)
friends.remove(12345)
print(friends)

#We can add items in list 

#Slicing in list

print(friends[1:4])
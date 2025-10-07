list = [0,7,3,1,4,22,5,5,5,99]
list.sort()
print(list)
list.reverse()
print(list)

list2 = []

for i in range(len(list)):
    if i == 0:
        list2.append(list[i])
    popped = list2.pop()
    if popped == list[i]:
        list2.append(popped)
        continue
    else :
        list2.append(popped)
        list2.append(list[i])

print(list2)
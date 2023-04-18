li = [1,2,3,4,5,6,7]

print(li)
print(li[2])

li.pop(4)
print(li)

li.append(5)
print(li)

print(li.count(2))

li.extend([11,33,44])
print(li)

l2 = li.copy()

print(l2)

li.append(56)
print(li)
print(l2)

l11 = [1,3,6,9,4]
l12 = l11

print(l11)
print(l12)

l11.append(23)
print(l11)
print(l12)

l11.insert(2,4)
print(l11)

l11.remove(4) #removes first occurence of any particular value
print(l11)
l11.remove(4)
print(l11)

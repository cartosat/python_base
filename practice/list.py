lis = [1, 1, 1, 2, 2, 2, 2, 3, 4, 5]

# extend
lis.extend([6, 7, 8])
print(lis)

# append
lis.append([0, 0, 0, 0])
print(lis)

lis = [1, 1, 1, 2, 2, 2, 2, 3, 4, 5]

# count of specific element from list.
print(lis.count(1))

# insert
lis.insert(0, 10)
print(lis)

# pop --> removes element at given index and return popped element.
print("---------")
print(lis.pop(0))
print("---------")

# remove --> Removes first occurence of given element
lis.remove(2)
print(lis)

# index
print(lis.index(2))

# reverse
lis.reverse()
print(lis)

# sort
lis.sort()
print(lis)

# copy --> creates shallow copy.
s1 = lis.copy()
print("Adress of s1:-", id(s1))
print("Adress of lis:-", id(lis))

# clear --> removes all element from list and list becomes empty.
lis.clear()
print(lis)


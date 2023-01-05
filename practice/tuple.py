
tuple = (1, 1, 1, 2, 2, 2, 2, 3, 4, 5)

print(tuple.count(2))
print(tuple.index(1))
print(tuple.index(2, 0, 4))

tuple = (1, 1, 1, 2, 2, 2, 2, 3, 4, 5)

#print(sorted(tuple)) # gives error
print(sum(tuple))

for i in tuple:
    print(i)
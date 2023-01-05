dictionary = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six'}

# get
print(dictionary.get(2))

# keys()
print(dictionary.keys())

# values
print(dictionary.values())

# items
print(dictionary.items())

print("------------------")
print(dictionary)
print("------------------")

# pop
print(dictionary.pop(6))
print(dictionary)

print("-------popitem-----------")
# popitem

print(dictionary.popitem())

print("-------popitem-----------")
print(dictionary)
dictionary.update({5:'five'})
print(dictionary)

# setdefault
print(dictionary.setdefault(5,'Six')) # this will return value of key, if key exists.
                                      # else it will add new key value pair if key does not exists.

print(dictionary.setdefault(6, 'six'))
print(dictionary)

# fromkey
keys = (8,9,10)

res = dict.fromkeys(keys)
print(res)

# clear
dictionary.clear()
print(dictionary) # return empty dict
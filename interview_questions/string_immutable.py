# Q: Why string are immutable explain with code




# Q: How do i modify a string in python?
# We can't modify string since they are immutable.
# We can construct new string from the various parts of existing string.
# In below example, although we have tried using list and assigning to same variable,
#  but id of first `s` and second `s` will be different.
s = list("Hello zorld")
print(id(s))
s[6] = 'W'
s = "".join(s)
print(s)
print(id(s))

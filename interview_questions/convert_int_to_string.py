# Q: How to convert int to string in Python

# Using str(integer)
# Using format() function
# Using the "%s" integer
# Using f-string

n = 10

print("Type of n:- ", type(n))

s1 = str(n)
print("Type of s1:- ", type(s1))

s2 = "{}".format(n)
print("Type of s2:- ", type(s2))

s3 = "%s"%n
print("Type of s3:- ", type(s3))

s4 = f"{n}"
print("Type of s4:- ", type(s4))


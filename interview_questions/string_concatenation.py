# Q: How to concatenate two strings in Python

# Using + operators
# Using join() method --> Join method accept iterables like list.
# Using % method
# Using format() function

s1 = "Vaibhav"
s2 = "Wagaskar"

s3 = s1 + s2
print(s3)

s4 = " ".join([s1, s2])
print(s4)

print("%s %s"%(s1, s2))

print("{} {}".format(s1, s2))

# Q : Reverse string

# Using the slice operator
# Using the reversed() function
# Using for loop
# Using while loop

s1 = "vaibhav"

# slice operator
print(s1[::-1])

# reversed function
print("".join(reversed(s1)))

# for loop
rev_s1 = ""
for i in range(len(s1) - 1, -1, -1):
    rev_s1 += s1[i]

print(rev_s1)

# while loop

count = len(s1)
rev_str = ""

while (count > 0):
    rev_str += s1[count - 1]
    count -= 1
print(rev_str)

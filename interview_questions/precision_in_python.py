# Q: How to Limit Floats to Two Decimal Points in Python

# Using “%”
# Using format()
# Using round(x,n)

a = 1.222323

# prints upto 2 decimals.
print("%.2f"%a)

# prints upto 3 decimals.
print("{0:.3f}".format(a))

# prints upto 4 decimals.
print(round(a, 4))
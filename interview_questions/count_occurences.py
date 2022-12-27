# Q: Count the occurrences of elements in the list.
# reference : https://protechstack.com/interview/python-interview-questions

lis = [1, 2, 4, 1, 1, 2, 3, 3]

# Using Counter function from collections module
from collections import Counter
di = Counter(lis)
print(di)

# Using pandas series function
from pandas import Series
sr = Series(lis)
print(sr.value_counts())

# User defined function
def value_counter(lis):
    co = {}
    for i in lis:
        if i in co.keys():
            co[i] += 1
        else:
            co[i] = 1
    return co

print(value_counter(lis))


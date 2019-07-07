
from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]


even=list(filter(lambda e:e%2==0,num))

print(num)
print(even)


def mul(n):
    return n*2

double=list(map(mul,even))

print(double)


def add(a,b):
    return a+b

sum=reduce(add,even)

print(sum)
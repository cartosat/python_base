'''a,b,c=[int(x)for x in input("Enter num:-").split('#')]
print(a+b+c)

from sys import argv
sum=0
args=argv[1:]
for x in args:
    n=int(x)
    sum+=n
print("sum=",sum)
print("avg=",sum/len(args))

import math as m
r=int(input("Enter radius"))
print("area of Circle is:-",m.pi*r*r)'''

#to find factorial of no first 10 nos from 0 using fact

def facto(n):
    return 1 if(n==1 or n==0) else (n*facto(n-1))
for x in range(1,10):
    print("factorial of:-",x,"is:-",facto(x))



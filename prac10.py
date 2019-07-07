from array import *
from numpy import *


KI=array([1,7,9,4,6,3])
VI=KI.view()

print(VI)

n=int(input("Enter the length of array:-"))

vals=array('i',[])

for i in range(1,n+1):
    z=int(input("Enter element:-"))
    vals.append(z)

print(vals)

s=int(input("Enter element to search:-"))
p=0
for d in vals:

    if d==s:
        print("key is found at:-",p+1)
        break
    p+=1




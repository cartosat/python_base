from array import *

vals= array('i',[1,5,2,3,6,7,9])

newArra=array(vals.typecode,(a for a in vals))

z=0


for e in newArra:
    print(e)

    z=z+e
print("Sum of numbers is :-",z)
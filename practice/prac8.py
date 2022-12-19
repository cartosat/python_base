from array import *

arr=array('i',[])

k= int(input("Enter size of array"))

for i in range(k):
    x=int(input("Enter no to insert:-"))
    arr.append(x)

print(arr)

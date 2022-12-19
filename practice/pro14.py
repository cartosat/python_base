from numpy import *

arr=array([1,3,5,7,9])

arr2=arr.view()


print("array 1",arr)
print("array 2",arr2)

print("ID array 1",id(arr))
print("ID array 2",id(arr2))

arr3=arr.copy()
print(arr3)

arr[1]=11
print("array 1",arr)
print("array 2",arr2)
print("array 3",arr3)
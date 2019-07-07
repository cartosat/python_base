from numpy import *

arr=array([ [1,2,3],
            [4,5,6],
            [7,8,9] ])

arr2=array([ [3,2,8],
            [2,9,1],
            [8,0,6] ])


m=matrix(arr)
p=matrix(arr2)

arr3=m*p

print(arr3)
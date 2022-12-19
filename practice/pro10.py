from array import *

vals=array('i',[1,2,8,9,7])
print(vals)
print(vals.buffer_info())
vals.reverse()
print(vals)

for a in vals:
    print(a)

newArr=array(vals.typecode,(p for p in vals))
print(newArr)

q=0
while q<=len(newArr):
    print(newArr[q])
    q+=1
from array import *

data=array('i',[])

index=int(input("Enter index value:-"))

for p in range(index):
    var=int(input("Enter next element:-"))
    data.append(var)

print(data)

key=int(input("Enter key to search:-"))

k=0
for e in data:
    if e==key:
        print(k)
        break

    k+=1
print(data.index(key))
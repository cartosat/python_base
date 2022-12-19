
i=20
def add():

   i=10
   j=3
   k=i+j
   v=globals()['i']
   print("loacal var i=",i)
   print(j)
   print(k)
   print("global v=",v)

print("global var i=",i)
add()
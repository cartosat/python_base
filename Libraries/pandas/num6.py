import numpy as np

a=np.matrix("3,1,2;3,2,5;6,7,8")
b=np.matrix("2;1;-3")

print(a)
print(b)
print(np.linalg.solve(a,b))


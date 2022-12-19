import numpy as np

a=np.matrix("1,2,3,4,5,6,7,8,9").reshape(3,3)

b=np.matrix("11,12,13,14,15,16,17,18,19").reshape(3,3)
a[0,0]=15

print(a)

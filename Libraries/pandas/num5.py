import numpy as np

x=np.matrix("1,1,1;1,1,1;1,1,1,")

det=np.linalg.det(x)
print(det)
rank=np.linalg.matrix_rank(x)
print(rank)


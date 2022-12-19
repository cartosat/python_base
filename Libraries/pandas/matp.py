import matplotlib.pyplot  as mp
import numpy as np

x=np.arange(start=0,stop=100,step=10)
yp=np.arange(start=0,stop=100,step=10)
yr=[]
for i in yp:
    p=(3.142/180)*i
    yr.append(p)

y=[]
for i in yr:
    d=np.sin(i)
    y.append(d)
print(x)
print(y)
mp.plot(x,y)
mp.show()
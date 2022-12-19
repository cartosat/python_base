import pandas as pd
dta=[1,2,3,4,5,6,7,8]
dat=['a','b','c','d','e']
data=[['Alex',10],['Bob',12],['Stark',15]]
dat=pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(dat)

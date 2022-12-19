import pandas as pd

data={'a':0,'b':5,'c':7,'d':15}
s=pd.Series(data,index=['c','d','e','a','b'])

print(s)
import pandas as pd
import numpy as np

data={'Name':['Tom','Jack','Steve'],'Age':[28,22,26]}

df=pd.DataFrame(data,index=['Rank1','Rank2','Rank3'])
print(df)
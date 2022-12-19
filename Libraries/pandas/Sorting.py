import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(10,2),index=[1,2,4,6,8,0,9,7,5,3],columns=['Col1','Col2'])

print(df)
sort_index=df.sort_index()
print(sort_index)
dort_column=df.sort_index(axis=1)
print(dort_column)
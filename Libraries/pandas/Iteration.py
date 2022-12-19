import pandas as pd
import numpy as np

'''N=20
df=pd.DataFrame({
    'A':pd.date_range(start='2016-05-01',periods=N,freq='D'),
    'x':np.linspace(0,stop=N-1,num=N),
    'y':np.random.rand(N),
    'c':np.random.choice(['Low','Medium','High'],N).tolist(),
    'D':np.random.normal(100,10,size=(N)).tolist()
})

for col in df:
    print(col)'''
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print(key,value)

for row_index,row in df.iterrows():
    print(row_index,row)

for row in df.itertuples():
    print(row)
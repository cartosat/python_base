import pandas as pd
dict={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([10,20,30,40],index=['a','b','c','d'])}

df=pd.DataFrame(dict)
df['three']=df['one']+df['two']
print(df)

import pandas as pd
import numpy as np
#Function
def Adder(num1,num2):
    return num1+num2

df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

print(df)
df.pipe(Adder,2)
print(df.apply(np.mean))
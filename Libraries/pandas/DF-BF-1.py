import pandas as pd
import numpy as np

dict={'Name':pd.Series(['Alex','John','Steve','Ricky','Vin','Smith','Jack']),
      'Age':pd.Series([25,22,23,27,22,22,25]),
      'Rating':pd.Series([4.23,3.6,4.12,3.68,4.5,3.89,4.0])}

df=pd.DataFrame(dict)
print(df)
print("Transpose is:",df.T)
print(df.axes)
print("Data type is:",df.dtypes)
print("is empty",df.empty)
print("dimension:-",df.ndim)
print("shape:",df.shape)
print("Size:",df.size)
print("Values:",df.values)
print("Head:",df.head(2))
print("Tail:",df.tail(2))

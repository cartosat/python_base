import pandas as pd
import numpy as np

dict={'Name':pd.Series(['Alex','John','Vaibhav','Kiran','Suraj','Rushi','Raj','Mayur']),
      'Age':pd.Series([21,22,21,28,29,19,25,11]),
      'Rating':pd.Series([3.14,3.52,4.0,4.2,3.9,3.0,4.8,4.3])}

df=pd.DataFrame(dict)
print(df.sum())
print(df.sum(1))
print("mean is:","\n",df.mean())
print("Bressel standard deviation of the numerical columns:","\n",df.std())
print("summary of statistics:\n",df.describe())

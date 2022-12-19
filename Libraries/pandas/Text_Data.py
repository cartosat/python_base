import pandas as pd
import numpy as np

df = pd.Series(['Tom', 'Rick', 'John', 'Alber@t', np.nan, '1234','smith'])
print(df)
print(df.str.lower())
print(df.str.upper())
print(df.str.len())
print(df.str.strip())
print(df.str.replace('@','$'))
print(df.str.swapcase())
print(df.str.islower())
print(df.str.isupper())
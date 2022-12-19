import pandas as pd
import numpy as np
so = pd.Series([1,2,3,4,5,4])
print(so)
print(so.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))
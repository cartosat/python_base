import pandas as pd
import numpy as np

data=pd.Series(np.random.randn(5))
print("The axes are:",data.axes)
print("Is object empty:",data.empty)
print("Dimension of objecct:",data.ndim)
print("Size of data:",data.size)
print("Actual series is :",data.values)
print("First two rows are:",data.head(2))
print("last two rows are:",data.tail(2))

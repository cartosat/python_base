import pandas as pd

data=[{'a':1,'b':2,'c':3},{'d':3,'e':5},{'a':8,'b':82,'c':23}]

pf=pd.DataFrame(data,index=['First','Second','Third'])
print(pf)
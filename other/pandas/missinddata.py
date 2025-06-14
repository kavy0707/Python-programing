import pandas as pd
import numpy as np

data = np.array("1,2,3,4,5,Nan")
data = pd.Series([1,2,3,4,np.nan,6,None])
print(data)
print()
print()
print()
print(data.isnull())
print()
print()
print()
print(data[data.isnull()])
print()
print()
print()
print(data.dropna())
print()
print()
print()
print(data.fillna(int(data.sum())))

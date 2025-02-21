import os
import numpy as np
import pandas as pd
os.chdir("D:\kavy\Python\Assigment-4")
data = pd.read_csv("_4program.csv")
data = pd.DataFrame(data)
print(data)
print("duplicate data:",data.duplicated())
print()
print()
print()
print()
print("duplicate data:",data.isnull())
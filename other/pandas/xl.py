import pandas as pd
import os

os.chdir(r'D:\kavy\Python\other\pandas')
a = pd.read_excel('test.xlsx')
print("Columns in the DataFrame:", a.columns)
a = a.set_index(["name", "Enroll"])  
print(a)
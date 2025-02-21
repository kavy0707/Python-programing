import pandas as pd
import os
os.chdir('D:/kavy/Python/other/pandas')
df = pd.io.parsers.read_csv('data.csv')
print(df.to_string())
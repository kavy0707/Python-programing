import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns



os.chdir(r'D:\kavy\Python\theory\Assigment-2')
data = pd.read_csv("data.csv")
# print(pd.DataFrame(data))
print(data.head())
print()
print()
print()
print(data.info())
print()
print()
print()
data_clean = data.dropna()
print(data_clean)
print()
print()
print()
print(data.describe())


# Group by liked status and calculate mean
liked_analysis = data.groupby('liked').count()
print(liked_analysis)


plt.plot(data['danceability'], data['energy'], marker="o", linestyle='')  # Empty linestyle for just points
plt.title('Danceability vs Liked')
plt.xlabel('Danceability')
plt.ylabel('Liked')
plt.show()

sns.scatterplot(data=data,x='danceability',y='energy')
plt.title('Danceability vs Liked')
plt.xlabel('Danceability')
plt.ylabel('Liked')
plt.show()


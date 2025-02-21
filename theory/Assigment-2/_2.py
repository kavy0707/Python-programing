import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data for exam scores
exam_data = {
    'name': ['Deep', 'Miral', 'Aesha','Khushi', 'Mihir', 'Charmi', 'Prachi', 'Priyanka', 'Abhishek', 'Yash'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
} 

# Labels for rows
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

# Creating DataFrame with all fields from exam_data and labels as index
exam_dataframe = pd.DataFrame(exam_data, index=labels)

# Printing the DataFrame with 'Name' and 'Score' columns
print(exam_dataframe[['name', 'score']])
print()
print()
print()
mis_score = exam_dataframe[exam_dataframe['score'].isna()]
print(mis_score)
print()
print()
print()
bet_score = exam_dataframe[exam_dataframe['score'].between(15,20)]
print(bet_score)


plt.plot(exam_dataframe['name'], exam_dataframe['score'], marker='o')
plt.title("Name vs. Score graph")
plt.xlabel("Name")  
plt.ylabel("Score")  
plt.xticks(rotation=45)  # Rotating x-axis labels for readability
plt.grid("true")
plt.show()
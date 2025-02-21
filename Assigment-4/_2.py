import numpy
import pandas as pd

# Use lists instead of sets
data = {
    "name": ["Kavy", "Jay", "Kishan"],
    "Enroll": ["23", "43", "28"]
}


data = pd.DataFrame(data)

data.to_csv(r'D:/kavy/PYTHON/Assigment-4/createdfile.csv')
print(data)

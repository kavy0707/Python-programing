import pandas as pd

data = {
    "A":[0,0,0,1,1,1],
    "B":[1,1,2,3,4,5],
    "C":[2,2,3,5,6,1]
}
data = pd.DataFrame(data)
groupA = data.groupby("A").describe()
print(groupA)


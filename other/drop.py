import pandas as pd

data = pd.DataFrame({
    "a" : [1,2,3],
    "b" : [4,5,6],
    "c" : [7,8,9]
})
print(data)
print()
print()
print()
drop_raw = data.drop(index=1)
print(drop_raw)
print()
print()
print()
drop_column = data.drop(columns="b")
print(drop_column)

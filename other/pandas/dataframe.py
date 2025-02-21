import pandas as pd

data = {
    "name" : ["kavy","kishan","ravi"],
    "enroll" : [23,28,29]
}

seriesdata = pd.DataFrame(data)
print(seriesdata)
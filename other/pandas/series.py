import pandas as pd

data = {
    "name" : ["kavy","kishan","ravi"],
    "enroll" : [23,28,29]
}

seriesdata = pd.Series(data)
print(seriesdata)

print()
print()
print()
a = ["x","y","z"]
myvar = pd.Series(a,index=[10,1,2])
print(myvar)
print("at indexz 1",myvar[1])




import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar1 = pd.Series(calories)
print(myvar1)

print()
print()
print()
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2= pd.Series(calories, index = ["day1", "day2"])
print(myvar2)
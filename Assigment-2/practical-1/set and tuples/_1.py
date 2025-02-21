# Add a list of elements to a given set

# set1 = {"Yellow", "Orange", "Black"}
# List1 = ["Blue", "Green", "Red"]

# Output = {'Yellow', 'Orange', 'Black', 'Blue', 'Green', 'Red'}


set1 = {"Yellow", "Orange", "Black"}
List1 = ["Blue", "Green", "Red"]



for i in range(0,len(List1)):
    set1.add(List1[i])

print(set1)
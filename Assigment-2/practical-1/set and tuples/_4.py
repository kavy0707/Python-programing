# Remove duplicate from a list and create a tuple and find the minimum and maximum number

List1 = [87, 45, 41, 65, 94, 41, 99, 94]

List1 = set(List1)
print(List1)

List1 = tuple(List1)
print(type(List1))
List1 = list(List1)

List1.sort()
print("min:",List1[0])
print("max:",List1[len(List1)-1])



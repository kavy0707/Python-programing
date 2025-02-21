# Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# list1 = [5, 10, 15, 20, 25, 50, 20]

# Output = [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]
x = list1.index(20)
list1.remove(20)
list1.insert(x,200)
print(list1)


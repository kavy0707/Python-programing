#  Add item 7000 after 6000 in the following Python List

# list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]

# Output = [10, 20, 300, 400, 5000, 6000, 7000, 500, 30, 40]

list1 = [10, 20, 300, 400, 5000, 6000, 500, 30, 40]
print(list1)
x = list1.index(6000)
list1.insert(x+1,7000)

print("after adding 7000 :",list1)


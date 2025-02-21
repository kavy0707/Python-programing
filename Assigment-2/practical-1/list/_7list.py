#  Given a Python list, remove all occurrence of 20 from the list

# list1 = [5, 20, 15, 20, 25, 50, 20]

# Output = [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in range(len(list1)-1,-1,-1):
    if(list1[i] == 20):
        list1.remove(list1[i])

print(list1)

list2= [5, 20, 15, 20, 25, 50, 20]
list2 = [x for x in list2 if x!=20]
print(list2)
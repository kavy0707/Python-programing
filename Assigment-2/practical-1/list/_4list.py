# Concatenate two lists in the following order

# list1 = ["Hello ", "Hi "]
# list2 = ["Dear", "Sir"]

# Output : ['Hello Dear', 'Hello Sir', 'Hi Dear', 'Hi Sir']


list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]
list3 = []

for i in range(0,2):
    for j in range(0,2):
        list3.append(list1[i]+list2[j])


print(list3)
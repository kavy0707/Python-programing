# 3. Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

# Original list  [34, 54, 67, 89, 11, 43, 94]
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]


list1=[34,54,67,89,11,43,94]


print(list1)
x=list1[4]
list1.remove(list1[4])

print("After removing 4 index",list1)

list1.insert(2,x)
print("After insert at 2 index",list1)

list1.insert(len(list1),x)
print("After insert at last index",list1)
# Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from the second.

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listthird = []

for i in range(0,len(listOne)):
    if(i%2 !=0):
        listthird.append(listOne[i])

for i in range(0,len(listTwo)):
    if(i%2 ==0):
        listthird.append(listTwo[i])


print(listthird)
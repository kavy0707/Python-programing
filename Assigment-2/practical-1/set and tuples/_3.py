#  Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set

# firstSet = {27, 43, 34}
# secondSet = {34, 93, 22, 27, 43, 53, 48}

# First Set  set()
# Second Set  {93, 22, 53, 48}

firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}

if(firstSet < secondSet):
    secondSet -= firstSet
    firstSet.clear()

else:
    print("first set is super set")

print(firstSet)
print(secondSet)

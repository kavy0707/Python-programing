# Check if all items in the following tuple are the same

A = (45, 45, 45, 45)
B = (10, 10, 45, 10)

def checksameelement(tuples):
    tuples = set(tuples)

    if (len(tuples) == 1):
        print("same")
    
    else:
        print("not same")

print("all element of tuple A are",end=" ")
checksameelement(A)
print("all element of tuple B are",end=" ")
checksameelement(B)
# Given a following two sets find the intersection and remove those elements from the first set

# First Set  {65, 42, 78, 83, 23, 57, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

Set1 = {65, 42, 78, 83, 23, 57, 29}
Set2 = {67,73,43,48,83,57,29}

inter = Set2.intersection(Set1)
print("Intersaction set =",inter)

Set1 = Set1 - inter
print("Updated set1 = ",Set1)
# Suppose there is a circle. There are petrol pumps 
# on that circle. Petrol pumps are numbered to
# (both inclusive). You have two pieces of
# information corresponding to each of the petrol
# pump: (1) the amount of petrol that particular
# petrol pump will give, and (2) the distance from
# that petrol pump to the next petrol pump.

# Initially, you have a tank of infinite capacity
# carrying no petrol. You can start the tour at any
# of the petrol pumps. Calculate the first point from
# where the truck will be able to complete the
# circle. Consider that the truck will stop at each of
# the petrol pumps. The truck will move one
# kilometer for each litre of the petrol.
    
# Input Format
# The first line will contain the value of.
# The next lines will contain a pair of integers
# each, i.e. the amount of petrol that petrol pump
# will give and the distance between that petrol
# pump and the next petrol pump.

# Output Format
# An integer which will be the smallest index of the
# petrol pump from which we can start the tour.


# Sample Input
# 3
# 1 5
# 10 3
# 3 4

# Sample Output
# 1

petrol = []
distance = []
number_pumps = int(input("Enter the number of petrol pumps: "))

for i in range(number_pumps):
    # Correct way to append elements to the list
    petrol.append(int(input(f"Enter the amount of petrol in pump {i + 1}: ")))
    distance.append(int(input(f"Enter the distance from pump {i + 1} to pump {i + 2}: ")))

petrol.sort()
print("Pump with the least petrol has:", petrol[0])
num = int(input("ENter the num to find series:"))

x=0
y=1

print(f"{x},{y}",end=",")

for i in range(2,num):
    sum = x + y
    print(sum,end=",")
    x = y 
    y = sum
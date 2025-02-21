# empty_list = []

# for i in range(1, 9):
#     for j in range(0, i):
#         empty_list.append(pow(2, j))
#     for k in range(len(empty_list) - 1, -1, -1):
#         print(empty_list[k], end=" ")
#     empty_list = []  
#     print() 

# for i  in range(1,9):
#     for j in range(i-1,-1,-1):
#         print(pow(2,j),end=" ")
#     print("")

x=0
y=1

print(x,y)
for i in range(3,6):
    z = x+ y 
    print(z,end=" ")
    x=y
    y=z
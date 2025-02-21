num = int(input("Enter the name:"))

count = 0
for i in range(2,num):
    if(num%i==0):
        count = 1

if(count==1):
    print("num is not  prime")
else:
    print("num is  prime")

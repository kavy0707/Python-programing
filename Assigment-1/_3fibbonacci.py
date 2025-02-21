mylist = [1, 2]

sum_even = 0
x = 1
y = 2

print(x, y, end=" ")

for i in range(3, 40):  
    z = x + y
    if z < 4000000:
        print(z, end=" ")
        mylist.append(z)  
        x = y
        y = z
    else:
        break

print()  

for num in mylist:
    if num % 2 == 0:
        sum_even += num

print("\nSum of even Fibonacci numbers:", sum_even)


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

smaller = min(x,y)
count = 0

if x < pow(10, 12) and y < pow(10, 12):
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            count = count + 1

print(count)

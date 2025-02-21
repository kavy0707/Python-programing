num = int(input("Enter number to find factorial:"))
fact = 1
for i in range(num,0,-1):
    fact = fact * i


print("factorial of the entered num is:",fact)
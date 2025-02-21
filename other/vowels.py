name = input("Enter the String:")
count = 0
vowels = "AEIOUaeiou"
for i in range(len(name)):
    if name[i] in vowels:
        count+=1

print(f"vowels count:{count}")
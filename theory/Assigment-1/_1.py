# Write a Python program to get a string made of
# the first 2 and the last 2 chars from a given a
# string. If the string length is less than 2, return
# instead of the empty string.
# Sample String: 'dipesh'
# Expected Result : dish
# Sample String : 'd'
# Expected Result : Empty String

name = input("Enter the string:")

if len(name)<=2:
    print("Empty string")
else:
    New_str = name[:2] + name[len(name)-2:]
    print(New_str)

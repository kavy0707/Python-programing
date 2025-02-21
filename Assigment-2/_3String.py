# Given a string which contains lower alphabetic characters, we  need to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.

# Input : abbccdd
# Output : Yes , We can remove 'a' from above string to make the frequency of each character same.
# Input : abcdd
# Output : Yes , We can remove 'd' from above string to make the frequency of each character same.
# Input : aabbbcccdddd
# Output : No , We can't remove any character from above string to make the frequency of each character same.


name="aabbbcc"
frequency= []
print(name)
for i in range(0,len(name)):
    frequency.append(name.count(name[i]))
print(max(frequency))



# if(count>1):
#     print("No , We can't remove any character from above string to make the frequency of each character same")
# else:
#     print("Yes , We can remove ",removed ," from above string to make the frequency of each character same.")
    
# print()

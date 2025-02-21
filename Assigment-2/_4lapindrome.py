#  Lapindrome is defined as a string which when split in the middle,gives two halves having the same characters and same frequency   of  each character. If there are odd number of characters in the      string, we ignore the middle character and check for lapindrome.

# For example , abccab, rotor and xyzxy are a few examples of lapindromes.
# Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.


name = input("enter the name:")

if((len(name)%2) == 0):
    i=int(len(name)/2)
    # print(i)


    list1=name[:i]
    # print(list1)
        
    list2=name[i:]
    # print(list2)

    if(sorted(list1) == sorted(list2)):
        print("It is a lapindrome")
    else:
        print("It is not a lapindrome")
     

else:
    i=int(len(name)/2)
    list1 = name[:i]
    list2 = name[i+1:]

    if(sorted(list1) == sorted(list2)): 
        print("It is a lapindrome") 
    else:
        print("It is not a lapindrome")
     
    

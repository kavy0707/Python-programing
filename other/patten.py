raw = int(input("Enter the number of raws"))

def patten(raw):
    for i in range(raw,0,-1):
        if(i%2!=0):
            print("$"*i)

    for i in range(2,raw+1):
        if(i%2!=0):
            print("$"*i)

patten(raw)
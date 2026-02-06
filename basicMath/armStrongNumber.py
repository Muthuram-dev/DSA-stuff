n = input("Enter the value: ")

orginal = int(n)



def armStrongNumber(n):
    finalNum = 0
    power = len(n)
    for i in n:
        digit = int(i)
        # print(type(digit))
        digit = digit ** power
        finalNum += digit
        
    if finalNum == orginal:
        print("TRUE")
    else:
        print("FALSE")

armStrongNumber(n)


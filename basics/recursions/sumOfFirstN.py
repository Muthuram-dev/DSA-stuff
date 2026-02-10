n = int(input("Enter the no: "))

def addition(n):

    if n == 0:
        return 0
    return n + addition(n-1)


print(addition(n))
n = int(input("Enter the no: "))

def increase(n):
    if n == 0:
        return
    increase(n-1)
    print(n)

increase(n)
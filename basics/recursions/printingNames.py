n = int(input("Enter: "))
name = "Sriram"


def recursion(n):
    if n < 1:
        return
    print(name)

    n -= 1
    recursion(n)
recursion(n)
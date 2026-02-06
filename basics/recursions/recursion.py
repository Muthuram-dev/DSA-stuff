def addition(n):
    if n > 100:
        return ""
    print(n)
    addition(n+1)
addition(1)
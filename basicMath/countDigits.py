n = int(input("Enter the value: "))
a = n
count = 0

# strNumber = str(n)
# lenght = len(strNumber)

if n == 0:
    count = 1

elif n>0:
    while n>0:
        n = n//10
        count += 1
else:
    print("Enter a valid number")



print(f"The number {a} has {count} digits")
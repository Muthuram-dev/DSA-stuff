n = int(input("Enter the value: "))

listOfDivisors = []

for i in range(1,n+1):
    if n % i == 0:
        listOfDivisors.append(i)
    else:
        None

        
print(listOfDivisors)
    
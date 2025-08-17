n = int(input("Enter the value: "))
original = n

#Easiest Solution using the string
# strNumber = str(n)
# print(strNumber[::-1])

#Solution 2 using the math concept

reversedNum = 0
while n>0:
    digits = n % 10
    reversedNum = reversedNum * 10 + digits
    n = n // 10

print(f"The reversed number of {original} is {reversedNum}")



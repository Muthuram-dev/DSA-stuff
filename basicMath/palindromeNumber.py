n = int(input("Enter the value: "))
original = n

#Mathematical approach
reversedNum = 0
while n>0:
    digit = n % 10
    reversedNum = reversedNum * 10 + digit
    n = n // 10

if original == reversedNum:
    print("it's a palindrome")
else:
    print("It's not a palindrome")

#String approach

# if strNum == strNum[::-1]:
#     print("It's a palindrome number")
# else:
#     print("No, it's not a palindrome number")
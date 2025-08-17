a = int(input("Enter the value: "))
b = int(input("Enter the value: "))

on1 = a
on2 = b

while b != 0:
        a, b = b, a % b
print(f"The GCD of {on1} and {on2} is {a}")

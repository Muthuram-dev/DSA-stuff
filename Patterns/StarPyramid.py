N = int(input("Enter the value: "))
for i in range(1, N + 1):
    spaces = " " * (N - i)
    stars = "*" * ((2 * i) - 1)
    print(spaces + stars)

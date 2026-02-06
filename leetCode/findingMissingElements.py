arr = [13,1,2,3,5,11,4,6,7]
max = 0

for i in arr:
    if i>max:
        max = i
    elif len(arr) == 0:
        print(-1)
print(max)

    
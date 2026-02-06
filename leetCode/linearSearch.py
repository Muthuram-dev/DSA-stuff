arr = [1,2,3,4,5,7]
target  = 69
if len(arr) == 0:
    print(-1)
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break
    elif target not in arr:
        print(-1)
        break

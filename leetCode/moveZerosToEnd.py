arr = [1,2,3,8,4,5,6]
slow = 0
for fast in range(1, len(arr)):
    if arr[slow] == 0:
        slow += 1
        arr[slow] = arr[fast]
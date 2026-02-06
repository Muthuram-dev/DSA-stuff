arr = [1,2,3,8,4,5,6]
arr1 = []
for i in range(1, len(arr)):
    arr1.append(arr[i])
arr1.append(arr[0])
print(arr1)
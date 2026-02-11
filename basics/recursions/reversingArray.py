arr1 = [1,2,3,4,5,6]

def reverseingArray(arr):
    p1 = 0
    p2 = len(arr) - 1
    while p1<p2:
        arr1[p1], arr1[p2] = arr1[p2], arr1[p1]
        p1 +=1
        p2 -=1
    print(arr)
reverseingArray(arr1)
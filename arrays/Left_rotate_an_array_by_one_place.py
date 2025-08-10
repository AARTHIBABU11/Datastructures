def left_rotate(arr):
    n = len(arr)
    a=arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
       
    arr[n-1] = a
    return arr

arr = [1,2,3,4,5]
print(left_rotate(arr))
       
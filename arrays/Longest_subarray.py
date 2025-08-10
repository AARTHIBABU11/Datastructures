def longest_subarray(arr,key):
    max_length = 0
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i,n):
            for k in range(i,j+1):
                s += arr[k]
                if s == key:
                    max_length = max(max_length,j-i+1)

    return  max_length

arr = [1,-1,1,1,1,1]
key = 3
print(longest_subarray(arr,key))
         
#optimal approach
def longest_subarray_opti(arr, key):
    l, r = 0, 0
    n = len(arr)
    s = 0
    max_len = 0

    while r < n:
        s += arr[r]

        # Shrink window if sum > key
        while s > key and l <= r:
            s -= arr[l]
            l += 1

        # Update max_len if sum == key
        if s == key:
            max_len = max(max_len, r - l + 1)

        r += 1

    return max_len

# Test
arr = [1, 2, 1, 2, 1]
key = 3
print(longest_subarray_opti(arr, key))  # Output: 4

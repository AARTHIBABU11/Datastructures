from itertools import permutations

nums = [1,2,3]
all_perms = list(permutations(nums))
print(all_perms[1])

def next_permutation(arr):
    n = len(arr)
    ind = -1
    # To fimd the break point
    for i in range(n-2 , -1 ,-1):
        if arr[i] < arr[i+1]:
            ind = i
            break
    
    if ind == -1:
        arr.reverse()
        return arr
    
    for i in range(n-1,ind):
        if arr[i] > arr[ind]:
            arr[i],arr[ind] = arr[ind],arr[i]

    arr[ind+1:] = reversed(arr[ind+1:])

    return arr

        


nums = [1,2,3,4,1,5,6,7,8]
print(next_permutation(nums))

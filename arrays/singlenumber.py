def singlenumber(arr):
    hash = {}
    for i in range(len(arr)):
        hash[arr[i]] = hash.get(arr[i],0)+1
        
    for key in hash:
        if hash[key] == 1:
            print(key)
    
arr = [2,6,2,3,3]
singlenumber(arr)


def singlenumberopti(arr):
    result = 0
    for num in arr:
        result ^= num
    
    return result
    
arr = [2,6,2,3,3]
print(singlenumberopti(arr))





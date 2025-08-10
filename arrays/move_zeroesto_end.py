#Brute Force 
def move_zeroes_to_end(arr):
    new = []
    for num in arr:
        if num != 0:
            new.append(num)

    while len(new) < len(arr):
        new.append(0)

    return new

arr = [1,0,2,0,0,0,0,3,6,7]
print(move_zeroes_to_end(arr))


#optimal approach
def move_zeroes_to_end_opti(arr):
        pos = 0
        for i in range(len(arr)):
             if arr[i] != 0:
                  arr[pos] , arr[i] = arr[i],arr[pos]
                  pos += 1
        
        return arr


arr = [1,0,2,0,0,0,0,3,6,7]
print(move_zeroes_to_end_opti(arr))

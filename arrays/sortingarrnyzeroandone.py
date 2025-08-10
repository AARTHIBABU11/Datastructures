def sortanarr(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]

    return arr



    
arr = [1,0,1,1,0,0]
print(sortanarr(arr))

def sortanarropti(arr):
    
    l ,mid = 0,0
    h  = len(arr)-1
    while mid <= h:
        if arr[mid] == 0:
            arr[l] , arr[mid] = arr[mid] , arr[l]
            l += 1
            mid += 1

        elif arr[mid] == 2:
            arr[h] , arr[mid] = arr[mid] , arr[h]
            h -= 1

        else:
            mid += 1

    return arr



    
arr = [1,0,1,1,0,0]
print(sortanarropti(arr))


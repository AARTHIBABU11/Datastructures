#Brute Force approach
def left_rotate(arr):
    new = arr[:3]
    old = arr[3:]
    
    
    return old + new

#T(C) = O(n)
#S(c) = O(n)


arr = [1,2,3,4,5,6,7,8,9]
print(left_rotate(arr))

#optimal approah
def leftrotate_optimal(arr,k):
    n = len(arr)
    k = k%n
    def reverse(start,end):
        
          while start< end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -=1
    #reverse the whole
    reverse(0,n-1)
    #reverse 1st k elements
    reverse(-k,n-1)
    #reverse the rest
    reverse(0,(n-k)-1)

    return arr


arr = [1,2,3,4,5,6,7]
k = 3
print(leftrotate_optimal(arr,k))

#T(C) = O(n)
#S(c) = O(1)
# Brute force
def right_rotate(arr):
    new = arr[-3:]
    old = arr[0:-3]
    
    
    return  new + old




arr = [1,2,3,4,5,6,7]
print(right_rotate(arr))
#T(C) = O(n)
#S(c) = O(n)

#The optimal approch of right rotate will be 
def rightrotate_optimal(arr,k):
    n = len(arr)
    k = k%n
    def reverse(start,end):
       
          while start< end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -=1
    #reverse the whole
    reverse(0,n-1)
    #reverse 1st k elements
    reverse(0,k-1)
    #reverse the rest
    reverse(k,n-1)

    return arr


arr = [1,2,3,4,5,6,7]
k = 3
print(rightrotate_optimal(arr,k))

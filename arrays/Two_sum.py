#Brute force 
def twos_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] + arr[i] == target:
                return i,j
        
       

arr = [2,11,8,7]
target = 9 
print(twos_sum(arr,target))

#T(c):O(N^2)  
#S(C):O(N)
#optimal solution
def twos_sum(arr,target):
    hash = {}
    for i,num in enumerate(arr):
        diff = target - num 
        if diff in hash:
            return (hash[diff],i)
        
        hash[num] = i
arr = [2,11,8,7]
target = 9 
print(twos_sum(arr,target))
        
#T(c):O(N)  
#S(C):O(1)



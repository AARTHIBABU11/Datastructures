#Brute Force approach
def missing(arr):
    n = len(arr)
   
    for i in range(n+1):
        if i not in arr:
             print(i)



arr = [3,2,0]
missing(arr)

#optimal approach
def missing_opti(arr):
   n = len(arr)
   actual_sum = sum(arr)
   expected_sum = n*(n+1)//2
   return expected_sum-actual_sum


arr = [3,2,0]
print(missing_opti(arr))
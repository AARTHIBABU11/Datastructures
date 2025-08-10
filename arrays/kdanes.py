#Brute force
def longest_subarray_with_sum_brute(nums):
    maximum = -float("INF")
    
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            sum = 0
            for k in range(i , j+1):
                sum += nums[k]

                maximum = max(maximum,sum)

       

    return maximum
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(longest_subarray_with_sum_brute(nums))
#T(C):O(n^3)
#S(C):O(1)
#Optimal approch
def longest_subarray_with_sum_better(nums):
    maximum = -float("INF")
    n = len(nums)
    for i in range(n):
        sums = 0
        for j in range(i,n):
            sums += nums[j]
            maximum = max(maximum,sums)

        

    return maximum
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(longest_subarray_with_sum_better(nums))
#T(C):O(n)
#S(C):O(1)



#Optimal approch
def longest_subarray_with_sum_opti(nums):
    maximum = -float("INF")
    sum = 0
    n = len(nums)
    for i in range(n):
        sum += nums[i]

        if sum > maximum:
            maximum = sum

        if sum < 0:
            sum = 0 

    return maximum
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(longest_subarray_with_sum_opti(nums))
#T(C):O(n)
#S(C):O(1)

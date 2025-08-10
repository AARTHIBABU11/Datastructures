#Brute force approach
def findMaxConsecutiveOnes(nums):
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count = 0 
            for j in range(i,len(nums)):
                if nums[j]  == 1:
                    count += 1
                else:
                    break 
            max_count = max(max_count , count)
        
    print(max_count)


nums = [1,1,0,1,1,1,1]
findMaxConsecutiveOnes(nums)

# optimal approach 
def findMaxConsecutiveOnesoptim(nums):
    max_count = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
             count += 1
             max_count = max(max_count , count)

        else:
            count = 0
        
    print(max_count)


nums = [1,1,0,1,1,1,1]
findMaxConsecutiveOnesoptim(nums)


            



        
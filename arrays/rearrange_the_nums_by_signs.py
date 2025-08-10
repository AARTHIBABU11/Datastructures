#Brute Force approach

def rearrange_the_nums(nums):
    negative = []
    positive = []
    for num in nums:
        if num<0:
            negative.append(num)
        else:
            positive.append(num)

    new = [] 
    for neg,pos in zip(negative,positive):
        new.append(pos)
        new.append(neg)

    return new

nums = [-3,1,-2,-5,2,4]
print(rearrange_the_nums(nums))

#Optimal approach 
def rearrange_the_nums_opti(nums):
    neg = []
    pos = []
    for num in nums:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)

    if len(pos) < len(neg):
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        # to fill remaining negatives at the end
        index = len(pos)
        for i in range(len(neg) - len(pos)):
            nums[index] = neg[len(pos)+i]
            index += 1

    else:
        for i in range(len(neg)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        # to fill remaining positives at the end
        index = len(neg)
        for i in range(len(pos) - len(neg)):
            nums[index] = pos[len(neg)+i]
            index += 1

    return nums

nums = [-3,1,-2,-5,2,4]
print(rearrange_the_nums(nums))



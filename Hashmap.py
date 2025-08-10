#To count numbers
arr = [4,5,6,7,8,8]
count = {}
for nums in arr:
    count[nums] = count.get(nums,0)+1

print(count)

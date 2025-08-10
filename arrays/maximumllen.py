#Brute force approach
arr = [12,2,3,4,4,4,4,46]
n = len(arr)
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            cnt +=1 
            if cnt > (n//2):
                ans = arr[i]
                
print(ans)


#T(C): O(n^2)
#S(C):O(n)

#brute force approach
from collections import Counter

arr = [1,2,3,4,5,4,5,3,5,5,5,5,5]
count = Counter(arr)
n = len(arr)
most_common_element =0
for key,val in count.items():
    if val > n//2:
        most_common_element = key
       
         
print(most_common_element)
#T(C): O(n)
#S(C):O(n)

#Optimal approch
def majorityelement(arr):
    cnt = 0
    ele = None
    n = len(arr)
    for i in range(n):
        if cnt == 0 :
            ele = arr[i]
            cnt += 1
        elif arr[i] == ele:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0
    for i in range(n):
        if arr[i] == ele:
            cnt1 += 1
        
    if cnt1 > n//2:
        return ele
    
arr = [3,6,2,7,2,2,2,2,2]   
print(majorityelement(arr))








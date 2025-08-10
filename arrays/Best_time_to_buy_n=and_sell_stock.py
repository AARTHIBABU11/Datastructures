#brute force approach
def buy_and_sell(arr):
    n = len(arr)
    max_profit = 0
    for i in range(n):
        for j in range(i+1 ,n):
            new = arr[j] - arr[i]
            max_profit = max(max_profit,new)

    return max_profit


arr = [11,1,3,1,9,10]
print(buy_and_sell(arr))

#T(C) = O(n^2)
#S(C) = O(n)

#brute force approach
def buy_and_sell_optimal(arr):
    min_price = arr[0]
    max_profit = 0
    for price in arr:
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

        if price < min_price:
            min_price = price 

    return max_profit



arr = [11,1,3,1,9,10]
print(buy_and_sell_optimal(arr))

#T(C) = O(n^2)
#S(C) = O(n)




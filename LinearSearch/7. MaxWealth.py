accounts = [[2,3,5],[5,10,12],[100]]

def findMaxWealth(arr):
    ans = 0 
    for i in range(len(accounts)):
        sum = 0
        for j in range(len(accounts[i])):
            sum = sum + accounts[i][j]
        if sum > ans:
            ans = sum
    return ans

print("max wealth = ",findMaxWealth(accounts))

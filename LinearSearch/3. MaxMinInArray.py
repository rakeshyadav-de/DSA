arr = [18,12,9,77,50,0]

def minNum(arr):
    minNum = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]<minNum):
            minNum = arr[i]
    return minNum

def maxNum(arr):
    maxNum = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>maxNum):
            maxNum = arr[i]
    return maxNum

print("maxNum => ",maxNum(arr))
print("minNum => ",minNum(arr))

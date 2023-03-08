arr = [[1,2,3],[0,22,3,4]]

def max(arr):
    maxVal = arr[0][0]    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j])>maxVal:
                maxVal = arr[i][j] 
    return maxVal
def min(arr):
    minVal = arr[0][0]    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j])<minVal:
                minVal = arr[i][j] 
    return minVal

print("max value in the arry is ",max(arr))
print("min value in the arry is ",min(arr))

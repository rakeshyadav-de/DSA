arr = [[1,2,3],[4,5,6,9]]

def linearSearchTwoDArray(arr,element):
    for i in range(0,len(arr)):
          for j in range(0,len(arr[i])):
                 if(arr[i][j]==element):
                       return True
    return False

out = linearSearchTwoDArray(arr,91)
if out == False:
      print('element not found in the array')
else:
      print('element  found in the array')
      
      
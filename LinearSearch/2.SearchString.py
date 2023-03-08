arr = "RakeshYadav"

def search(arr,element):
    if len(arr)==0:
        return False
    for i in range(0,len(arr)):
        if arr[i] == element:
            return True
    return False

out = search(arr,'R')    
print(out)
          
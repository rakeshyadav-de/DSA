arr = [18,124,9,1764,123, 3333,55]

def countNumEvenDigits(arr):
    count = 0 
    for i in range(len(arr)):
              
        if(len(str(arr[i])) % 2 == 0):
            count = count + 1 
    return count

def countDigits(num):
    count = 0
    if num == 0:
        return 1
    if num < 0 :
        num = num * -1 
    while num > 0 :
        count = count + 1
        num = num // 10        
    return count


def countNumEvenDigits1(arr):
    count = 0 
    for i in range(len(arr)):              
        if(countDigits(arr[i]) % 2 == 0):
            count = count + 1 
    return count

print("array contains ",countNumEvenDigits1(arr)," numbers with even digits")

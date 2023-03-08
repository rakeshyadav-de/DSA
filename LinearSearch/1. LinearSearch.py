arr = [18,12,9,77,50]

# check if 14 exists in the array or not.

def linearSearch(arr,searchElement):
    '''
    This function search if the element exists in the given array or not.
    :param arr: This is the array we need to pass to search 
    :param searchElement: This is the element which you are looking to search inside the array.
    :return: The result of the function, it returns -1 if the element does not exists in the array else it returns the index of the array

    '''
    for index in range(0,len(arr)):
        if(arr[index] == int(searchElement)):
            return index
    return -1 

output = linearSearch(arr,500)
if(output == -1):
    print("element does not exist in the array")
else:
    print("element exists at location => ",output)

# binary search 

def search(arr,item):
    low =0
    high = len(arr)-1
    while low <= high:
        mid =low + high
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess <item:
            low = mid +1
        else:
            high = mid + 1
    return None


print(search([1,1,5,7,8,9,10],10))
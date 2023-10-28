# you just forget about it 
def search(arr,item):
    low= 0
    high = len(arr)-1
    while low <= high:
        mid = (low+ high)
        guess= arr[mid]
        if item == guess:
            return mid
        elif item < guess:
            high = mid -1
        else:
            low = mid + 1
    return None


print(search([1,3,5,7,8,9],8))

# let's create a binary search algorithms


def search(arr,item):
    high= len(arr)- 1
    low = 0
    while low <= high:
        mid = high + low
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid +1
    return None


print(search([1,2,4,55,77], 77))
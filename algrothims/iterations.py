

# binary sort
def binarysearch(arr):
    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= 6: 
            right = mid
        else:
            left = mid + 1
    return left

arr = [1, 2, 3, 4, 5, 6, 7]
answer = binarysearch(arr=arr)
print("the number is", answer)
def binarysort(arr):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = left + (right - left ) // 2
        if arr[mid] >= 1:
            right = mid # target number
        else:
            left = mid + 1
        return left


arr = [1, 2, 3, 4, 5, 6, 7]

answer = binarysort(arr=arr)
print("answer is", answer)
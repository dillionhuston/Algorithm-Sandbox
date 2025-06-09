arr = [1, 2, 3, 4, 5, 6, 7, 8]

# binary search 


find = 3
found = False
startIndex = 0 
endIndex = len(arr) -1 # get lengh of numbers to get how many numbers and then take away 1 until finised

while startIndex <= endIndex:
    midpoint = endIndex + startIndex // 2 # need to get the firt index and last then divide it to find the middle point

    if arr[midpoint] == find:
        print('found at ', midpoint)
        found = True
        break

    if arr[midpoint] > find:
        endIndex = midpoint - 1
    else:
        startIndex = midpoint - 1

    if not found:
        print("notfound")
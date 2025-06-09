# merge sort, factorial, reverse

# just seperating each algro that uses recursion

def factorial(n)-> int:
    if n == 0:
        return 1
    else:
        return  n * factorial(n-1)



def mergesoirt(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_a



# brute force approach for finding the maximum and minimum elements in an array
# The time complexity of this approach is O(n)
# The brute force approach involves a single pass through the array with comparisons for each element,
def max_min_bruteforce(arr):
    if not arr:
        return None, None  
    
    max = arr[0]
    min= arr[0]

    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num

    return max, min

# Driver code
arr = [1, 10, 100, 99, 77, 88, 0, 8]
max_val, min_val = max_min_bruteforce(arr)
print(f"max: {max_val}\nmin: {min_val}")






# divide and conquer algorithm to find both the maximum and minimum elements in an array
# time complexity of O(n)
# Involve fewer total comparisons in practice due to the recursive nature of the algorithm.
def max_min(arr,p,q):
    if not arr:
        return None, None
    
    if p==q:
        max= min =arr[p]
    elif p == q-1:
        if arr[q]>arr[p]:
            max = arr[q]
            min = arr[p]
        else:
            max = arr[p]
            min = arr[q]
    else:
        mid = p + (q-p)//2
        maxL, minL =  max_min(arr, p, mid)
        maxR, minR = max_min(arr, mid+1, q)

        if maxR > maxL:
            max = maxR
        else:
            max = maxL
        
        if minL > minR:
            min = minR
        else:
            min = maxL    

    return max,min



#driver code 

arr= [1, 10, 100, 99, 77, 88, 0, 8, -1]
max,min = max_min(arr,p=0,q=len(arr)-1)


print(f"max:{max}\nmin:{min}")

    
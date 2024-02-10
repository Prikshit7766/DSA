# QuickSort
# Best-case time complexity:
# If the partition process always divides the array into two approximately equal halves,
# the time complexity is O(n log n) where 'n' is the number of elements in the array.
# This happens when the pivot divides the array into two nearly equal halves.

# Worst-case time complexity:
# The worst-case time complexity of QuickSort is O(n^2), which occurs when the pivot is always the smallest or largest element.
# This can happen, for example, if the array is already sorted in ascending or descending order,
# and the pivot is chosen as the first or last element without any further optimization.

def partition(arr, p, q):
    pivot = arr[p]  # set the pivot
    i = p
    j = p + 1

    while j <= q:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1  # Increment j pointer regardless

    arr[i], arr[p] = arr[p], arr[i]

    return i  # index of pivot element




def quicksort(arr,p,q):
    if p==q:
        return arr
    if p<q:
        m =partition(arr,p,q)
        quicksort(arr,p,m-1)
        quicksort(arr,m+1,q)


arr=[50,70,80,30,40,88,19,27,69]
quicksort(arr, 0, len(arr)-1)


print("number of inversion :", arr)
        
        
import random

def partition(arr, p, q):
    pivot_index = random.randint(p, q)  # Select a random pivot index
    arr[p], arr[pivot_index] = arr[pivot_index], arr[p]  # Move pivot to the beginning
    pivot = arr[p]  # Pivot is now the first element
    i = p
    j = p + 1

    while j <= q:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i], arr[p] = arr[p], arr[i]

    return i  # index of pivot element

def quicksort(arr, p, q):
    if p < q:
        m = partition(arr, p, q)
        quicksort(arr, p, m - 1)
        quicksort(arr, m + 1, q)

arr = [50, 70, 80, 30, 40, 88, 19, 27, 69]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
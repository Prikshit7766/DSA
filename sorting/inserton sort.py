def insertion_sort(arr):
    n = len(arr)

    # Best case: If the array is already sorted, the inner loop won't need to perform any shifts.
    # In this case, the time complexity is O(n), as the outer loop iterates once through the array.
    
    # Worst case: If the array is sorted in reverse order, each element will need to be compared and shifted to its correct position.
    # In this case, the time complexity is O(n^2), as each element may require up to 'i' comparisons and shifts,
    # where 'i' is the index of the outer loop.
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage:
my_array = [64, 25, 12, 22, 11]
insertion_sort(my_array)
print("Sorted array:", my_array)

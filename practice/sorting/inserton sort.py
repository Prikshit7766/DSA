def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        Value = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and Value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = Value

# Example usage:
my_array = [64, 25, 12, 22, 11]
insertion_sort(my_array)
print("Sorted array:", my_array)

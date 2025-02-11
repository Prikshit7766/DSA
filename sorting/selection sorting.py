# selection sort algo
#for each pass one swap is required so swap war minmum
# Time complexity : O(n^2)
# for each pass only one swap is required
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_array = [64, 25, 12, 22, 11]
selection_sort(my_array)
print("Sorted array:", my_array)





def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found in the list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5

result = linear_search(my_list, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found in the list')
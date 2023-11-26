def find_missing_values(arr):
    # XOR all elements in the array and all possible values
    xor_result = 0
    for num in arr + list(range(1, len(arr) + 3)):
        xor_result ^= num

    # Find the rightmost set bit
    rightmost_set_bit = xor_result & -xor_result   # find the right most  set bit  and give the outut in int
    print(rightmost_set_bit)

    # Initialize variables for the two missing values
    missing_value_1 = 0
    missing_value_2 = 0

    # XOR elements in the array based on the rightmost set bit
    for num in arr:
        if (num & rightmost_set_bit) == 0:
            print(num ,"&",rightmost_set_bit , "-->",num & rightmost_set_bit)
            missing_value_1 ^= num
        else:
            missing_value_2 ^= num

    # XOR possible values based on the rightmost set bit
    for num in range(1, len(arr) + 3):
        if (num & rightmost_set_bit) == 0:
            missing_value_1 ^= num
        else:
            missing_value_2 ^= num

    return missing_value_1, missing_value_2

# Example usage
arr = [1, 2, 4,6]
result = find_missing_values(arr)
print("Missing values:", result)
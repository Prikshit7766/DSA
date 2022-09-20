#source :- https://www.geeksforgeeks.org/find-two-missing-numbers-set-2-xor-based-solution/

def findTwoMissingNumbers(arr, n):
    XOR = arr[0]
    for i in range(1, n - 2):
        XOR ^= arr[i]
    for i in range(1, n + 1):
        XOR ^= i

    set_bit_no = XOR & ~(XOR - 1)


    x = 0
    y = 0
    for i in range(0, n - 2):
        if arr[i] & set_bit_no:


            # XOR of first set in arr[]
            x = x ^ arr[i]

        else:

            # XOR of second set in arr[]
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if i & set_bit_no:

            # XOR of first set in arr[] and
            # {1, 2, ...n }
            x = x ^ i


        else:

            # XOR of second set in arr[] and
            # {1, 2, ...n }
            y = y ^ i

    return x,y;


arr3 = [1,3,5]
n = 2 + len(arr3)
findTwoMissingNumbers(arr3,4)
print(findTwoMissingNumbers(arr3,4))


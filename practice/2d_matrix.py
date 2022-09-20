def search(mat, n, x):
    if (n == 0):
        return -1

    # Traverse through the matrix
    for i in range(n):
        for j in range(n):

            # If the element is found
            if (mat[i][j] == x):
                print("Element found at (", i, ",", j, ")")
                return 1

    print(" Element not found")
    return 0


# Driver code
mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
search(mat, 4, 50)
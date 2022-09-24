# the matrix should be sorted row vise

def searchMatrix(matrix , target: int):
    if not matrix or not matrix[0]:
        return False

    # finding out row
    for x in range(len(matrix)):

        if target == matrix[x][0] or target == matrix[x][-1]:
            return True

        elif target > matrix[x][0] and target < matrix[x][-1]:
            # look for element in row
            l, r = 0, len(matrix[x]) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if target == matrix[x][mid]:
                    return True

                elif target > matrix[x][mid]:
                    l = mid + 1

                else:
                    r = mid - 1

            return False



mat = [[10, 20, 30, 40],
       [50, 60, 70, 80],
       [90, 100, 110, 120]]


x=500

print(searchMatrix(mat ,x) )
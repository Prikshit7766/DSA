# the matrix should be sorted both row and column wise

def search_2d_sorted_matrix(mat,target):
    i=0
    j=len(mat[0])-1
    n=len(mat)
    while (i<n and j>0):
        if mat[i][j]==target:
            return (i,j)
        elif(mat[i][j])>target:
            j-=1
        else :
            i=i+1
    return  False

# Driver code
mat = [[1,4,7,11,15], 
       [2,5,8,12,19], 
       [3,6,9,16,22], 
       [10,13,14,17,24],
       [18,21,23,26,30]]

target=30
print(search_2d_sorted_matrix(mat,target))


# Time complexity order of n
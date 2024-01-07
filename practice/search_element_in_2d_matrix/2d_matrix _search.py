mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

x=50
l=len(mat)
for  i in range(l):
       for j in range(l):
              if mat[i][j]==x:
                     a=[i,j]
                     break

if not a:
    print("element is not present")
else:
       print(*a)


print(mat[a[0]][a[1]])
# brute force approch
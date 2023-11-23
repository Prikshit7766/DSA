mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

x=50
for  i in range(4):
       for j in range(4):
              if mat[i][j]==x:
                     a=[i,j]
                     break

if not a:
    print("element is not present")
else:
       print(*a)

# brute force approch
arr = [2, 3, 4, 10, 40,50]
x = 50
j=len(arr)
i=0
a=0
if i == j:
    if arr[i] == x:
        print(i)
    else:
         print(-1)
for i in range(j):
    mid=i+((j-i)//2)
    if arr[mid]==x:
        a=mid
        break
    elif arr[mid]<x:
        i=mid+1
    elif arr[mid]>x:
        j=mid-1
if a == 0:
    print("element is not present")

else:
    print(a)






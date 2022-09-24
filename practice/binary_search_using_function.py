# using recursion
def binary_search(arr,i,j,x):
    if j==i:
        if arr[j]==x:
            return i
        else:
            return -1
    else:
        mid=i+(j-i)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            return binary_search(arr,mid+1,j,x)
        else:
            return binary_search(arr,i,mid-1,x)

arr=[10,23,44,55,77,101]
i=0
j=len(arr)
x=77
ans=binary_search(arr,i,j,x)
print(ans)

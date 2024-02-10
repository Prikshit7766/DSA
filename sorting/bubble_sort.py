# Time complexity : O(n^2)
#Space Complexity : O(1)

def bubbleSort(arr,n):

    for i in range(n-1):
        #Laset i element is in sorted manner 
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                # Swap the elemnets of array[j] with array[j+1]
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr



arr = [64, 34, 25, 12, 22, 11, 90]
n=len(arr)

z=bubbleSort(arr,n)
print(*z)

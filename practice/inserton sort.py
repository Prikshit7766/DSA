def insertionSort(arr,j):

    while (j>=0 and value<arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=value



arr = [12, 11, 13, 5, 6]
for i in range (1,len(arr)):
    j=i-1
    value=arr[i]
    insertionSort(arr,j)


lst = []  # empty list to store sorted elements
print("Sorted array is : ",*arr)

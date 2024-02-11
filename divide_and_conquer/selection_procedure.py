def partition(arr, p, q):
    pivot = arr[p]
    i = p
    j = p + 1

    while j <= q:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i], arr[p] = arr[p], arr[i]

    return i




def selection_procedure(arr, p, q, k):
    if p==q:
        return arr[p]
    
    else:
        m = partition(arr,p,q)

        if m==k:
            return arr[m]
        elif m<k:
            return selection_procedure(arr, m+1, q, k)
        else:
            return selection_procedure(arr,p,m-1,k)
        



arr=[50,70,80,30,40,88,19,27,69]
print("Select the 3rd samllest number from the array :", selection_procedure(arr = arr, p = 0, q = len(arr)-1, k = 2))
        
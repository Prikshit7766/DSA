# brute force approach
# Time complexicity O(n^2)
def number_of_inversion1(arr):
    l = len(arr)
    count = 0
    for i in range(l-1):
        for z in range(i+1,l):
            if arr[i]> arr[z]:
                count+=1
    
    return count



arr = [70,50,60,10,20,30,80,15]

print("number of inversion :", number_of_inversion1(arr))
            

# Divide and conquer 
# Time complexicity O(nlogn)

def number_of_inversion2(arr):
    count = 0
    if len(arr)>1:
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:]
        count += number_of_inversion2(L)
        count += number_of_inversion2(R)
        count += merge(arr,L,R)
    return count

def merge(arr, L,R):
    count = i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            count += len(L) - i  # Counting inversions
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return count
    
     
arr = [70,50,60,10,20,30,80,15]

print("number of inversion :", number_of_inversion2(arr))
    
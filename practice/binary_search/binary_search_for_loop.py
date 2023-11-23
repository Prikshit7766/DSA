arr = [2, 3, 4, 10, 40, 50]
x = 3
j = len(arr) - 1
a = 0

for i in range(j + 1):
    mid = i + ((j - i) // 2)
    if arr[mid] == x:
        a = mid
        break
    elif arr[mid] < x:
        i = mid + 1
    else:
        j = mid - 1

if a == 0:
    print("Element is not present")
else:
    print(a)

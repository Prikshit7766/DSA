arr = [2, 3, 4, 10, 40, 50]
x = 3
a = 0

for i in range(len(arr)):
    mid = i + (len(arr) - i) // 2
    if arr[mid] == x:
        a = mid
        break
    elif arr[mid] < x:
        i = mid + 1
    else:
        arr = arr[:mid]

if a == 0:
    print("Element is not present")
else:
    print(a)

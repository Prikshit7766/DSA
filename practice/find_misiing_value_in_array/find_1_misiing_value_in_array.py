# 1 approch Hashing  :  Time complexity - > O(n)
print("1 approch")
arr1 = [0,1,3]
m=[]
for i in range(0,len(arr1)):
    if i not in arr1:
        arr1.append(i)
        m.append(i)

print(*arr1)
print("misiing value",*m)


# 2   :  By using the property of sum of n natural numbers  with Time complexity - >   O(n) operation of calculating the sum of the elements in the array

print("-------------------------------------------")
print("2 approch")
arr2 = [0,1,3,4]
s=sum(arr2)
n=len(arr2)

Total_sum=n*(n+1)//2
diff=Total_sum-s

arr2.append(diff)
print(*arr2)
print("misiing value",diff)


# 2 approch : By utilizing Xor approch (Bitwise manuplation)  Time complexity - > O(n) and space complexity = o(1)

print("-------------------------------------------")
print("3 approch(xor)")
arr3 = [0, 1, 4,3]

xor_arr = 0
for z in range(len(arr3)):
    print(xor_arr,"^", arr3[z] ,"^" ,z ,"-- >",xor_arr ^ arr3[z] ^ z)
    xor_arr = xor_arr ^ arr3[z] ^ z

missing_value = xor_arr ^ len(arr3)
arr3.append(missing_value)

print("-------------------------------------------")
print("Using XOR Operation:")
print(*arr3)
print("Missing value:", missing_value)



print("-------------------------------------------")
print("4 approch(xor)")
arr = [0, 1, 3, 4]
check_arr = list(range(len(arr) + 1))

result = 0

for num in arr + check_arr:
    result ^= num

print(result)






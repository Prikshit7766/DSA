# 1 approch
print("1 approch")
arr1 = [0,1,3]
m=[]
for i in range(1,len(arr1)+1):
    if i not in arr1:
        arr1.append(i)
        m.append(i)

print(*arr1)
print("misiing value",*m)


# 2 approch

print("-------------------------------------------")
print("2 approch")
arr2 = [1,3,4]
s=sum(arr2)
n=len(arr2)+1
j=0
Total_sum=n*(n+1)//2
diff=Total_sum-s
arr2.append(diff)
print(*arr2)
print("misiing value",diff)


# 2 approch

print("-------------------------------------------")
print("3 approch(xor)")
arr3 = [0,1,3]
index_arr =[]
xor_arr=0
for z in range(len(arr3)-1):
    xor_arr = xor_arr ^ arr3[z] ^ z
z+=1
xor_arr = xor_arr  ^ z
arr3.append(xor_arr)
print(*arr3)
print("misiing value",xor_arr)








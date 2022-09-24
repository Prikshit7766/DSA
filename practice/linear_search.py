def search(a,e):
    c=0
    for i in range(len(a)):
        if a[i]==e:
            return c
        else:
            c+=1
    return -1



arr=[1,2,3,44,556,88,101,22,33]
element=222222222
z=search(arr,element)

print(z)
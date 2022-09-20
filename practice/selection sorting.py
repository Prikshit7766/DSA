# selection sort algo
def sort_(a,min,i):
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min=j
    a[i], a[min] = a[min], a[i]   # swaping operation

a = [64, 25, 12, 22, 11,0,-1]
for i in range(len(a)):

     sort_(a,i,i)
     print(a)





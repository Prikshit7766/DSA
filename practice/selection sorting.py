# selection sort algo
#for each pass one swap is required so swap war minmum
def sort_(a,min_index,i):
    for j in range(i+1,len(a)):
        if a[min_index]>a[j]:
            min_index=j
    a[i], a[min_index] = a[min_index], a[i]   # swaping operation

a = [64, 25, 12, 22, 11,0,-1]
for i in range(len(a)):

     sort_(a,i,i)
print(a)





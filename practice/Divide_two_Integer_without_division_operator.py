# Brute foce approch (not optimized )
def quot(a,b):
    c=0
    while a>=b:
        a=a-b
        c+=1
    return  c


divident = 20
divisor = 3
print ("quotient",quot(divident,divisor))

#  approch optimized


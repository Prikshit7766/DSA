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

def op_quot(a,b):
    temp = 1
    ans = 0
    while a>=b:


        b << 1
        temp << 1
    while (temp>1):
        b>>1
        temp>>1
        if (a>=b):
            a-=b
            ans +=temp
    return ans


divident = 20
divisor = 3
q=op_quot(divident,divisor)
print(q)
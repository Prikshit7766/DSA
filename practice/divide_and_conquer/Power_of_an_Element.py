# divide_and_conquer

def DAC_Power(a,n):
    if n == 0:  #O(1)
        return 1
    elif n == 1:   #O(1)
        return a
    else:
        mid = n//2   #O(1)
        b = DAC_Power(a, mid) # T(n/2)
        c = b * b      # O(1)  This c = b * b  is for left and right sides 
        #n is even or odd 
        # constant time complexity
        if n % 2 == 0:
            return c
        else:
            return c * a     

print("power of an element is : ",DAC_Power(2,11))

#Time complexity : O(log n)
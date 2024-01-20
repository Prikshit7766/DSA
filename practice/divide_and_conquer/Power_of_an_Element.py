## Recurrence Relation -> T(n) = T(n/2) + c
## Master's Theorem -> T(n) = O(log n)
## Method Definition
## n >= 1 and a >= 2
def DAC_Power(a, n):
  # Small Problem
  if n == 1:
    return a
  else:
  # Big Problem --> Divide and Conquer Methodology
    mid = n//2  # O(1)
    b = DAC_Power(a, mid)   #T(n/2)
    # Important To Understand
    c = b * b         # O(1)
  # n is even or odd
  # Constant time complexity
    if n % 2 == 0:   
      return c
    else:
      return c * a

## Driver Code
a = 2
n = 16
result = DAC_Power(a, n)
print("Power of an Element is:", result)

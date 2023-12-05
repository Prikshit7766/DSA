def maxsubarray(arr)-> int:
    maxSub = arr[0]
    curSum=0


    for n in arr:
        if curSum<0:
            curSum=0
        
        curSum += n

        maxSub = max(maxSub, curSum)
    return maxSub


print(maxsubarray(arr=[2,-3,5,9,0,-9,1,7,-10]))

def canSum(m,num,memo={}):
    
    if m in memo:
        return memo[m]    
    if m==0:
        return True
    if m<0:
        return False
    
    for i in num:
        diff=m-i
        if canSum(diff,num,memo):
            memo[m]=True
            return True
    memo[m]=False
    return False



#Returns True if one can sum the target number using the numbers in the list.

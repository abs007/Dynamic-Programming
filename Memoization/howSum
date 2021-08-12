def howSum(tsum,num,memo={}):
    if tsum in memo:
        return memo[tsum]
    if tsum==0:
        return []
    if tsum<0:
        return None
    for n in num:
        rem=tsum-n
        remr=howSum(rem,num,memo)
        if remr!=None:
            remr+= [n]
            memo[tsum]= remr
            return memo[tsum]
    
    memo[tsum]=None
    return memo[tsum]



#Returns the different ways to compute the target using the numbers in the list.

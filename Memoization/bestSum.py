def bestSum(tsum,num,memo={}):
    if tsum in memo:
        return memo[tsum]
    if tsum==0:
        return []
    if tsum<0:
        return None
    
    scom= None
    for n in num:
        rem= tsum-n
        remc= bestSum(rem,num,memo)
        if remc!=None:
            remc+=[n]

            if scom is None or len(remc)<len(scom):
                scom=remc
    memo[tsum]=scom
    return scom



#Returns the shortest way to compute the target using the numbers in the list

def gridTraveller(m,n,memo={}):
    key = str(m)+','+str(n)
    if key not in memo:
        if m==0 or n==0:
            return 0
        elif m==1 and n==1:
            return 1
        else:
            memo[key]= gridTraveller(m-1,n,memo) + gridTraveller(m,n-1,memo)
    return memo[key]




#Return the number of ways one can travel from the top-left to the bottom-right in a 2d grid.

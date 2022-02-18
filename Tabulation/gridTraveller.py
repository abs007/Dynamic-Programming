def gridTraveller(m,n):
    table= [[0 for i in range(n+1)] for j in range(m+1)]
    table[1][1]=1
    
    for i in range(m+1):
        for j in range(n+1):
            if j+1<=n:
                table[i][j+1]+= table[i][j]
            if i+1<=m:
                table[i+1][j]+= table[i][j]
    
    print(table)
    return table[m][n]



#Return the number of ways one can travel from the top-left to the bottom-right in a 2d grid.

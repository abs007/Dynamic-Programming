def bestSum(target,num):
    table= [None for i in range(target+1)]
    table[0]= []
    d=None
    
    for i in range(len(table)):
        if table[i] is not None:
            for n in num:
                if i+n<=target:
                    c=list(table[i])
                    c+=[n]
                    if table[i+n] is not None:
                        if len(c)>=len(table[i+n]):
                            continue
                    table[i+n]=c
                
    print(table)
    return table[target] 

#Returns the shortest way to compute the target using the numbers in the list

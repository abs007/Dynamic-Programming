def howSum(target,num):
    table= [None for i in range(target+1)]
    table[0]= []
    
    for i in range(len(table)):
        if table[i] is not None:
            for n in num:
                if i+n<=target:
                    c=list(table[i])
                    c+=[n]

                    table[i+n]=c

    return table[target] 

#Returns the different ways to compute the target using the numbers in the list.

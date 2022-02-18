def canSum(target,num):
    table= [False for i in range(target+1)]
    table[0]=True
    
    for i in range(len(table)):
        if table[i]==True:
            for n in num:
                if i+n<=target:
                    table[i+n]=True

    return table[target]

#Returns True if one can sum the target number using the numbers in the list.

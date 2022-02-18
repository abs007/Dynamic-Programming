def canConstruct(target,words):
    table=[[] for i in range(len(target)+1)]
    table[0]=[[]]
    
    for i in range(len(target)):
        if len(table[i])>0:
            for w in words:
                if i+len(w)<=len(table)-1 and target[i]==w[0] and w[-1]==target[i+len(w)-1]:
                    for j in range(len(table[i])):
                        co=list(table[i][j])
                        co+=[w]
                        table[i+len(w)].append(co)



    return table[len(target)]

# Returns True if we can construct the target string using the words/letters in the list.

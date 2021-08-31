def allConstruct(target, words):
    if target=='':
        return [[]]
    result=[]
    for w in words:
        if target.find(w)==0:
            suffix = target.replace(w,'',1) 
            suffixways= allConstruct(suffix, words)
            targetways= [[w] + s for s in suffixways]
            result+=targetways
    return result
    
    
    
    
# Returns all the ways to construct the target string using the words/letters in the list.

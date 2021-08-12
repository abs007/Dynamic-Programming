def canConstruct(s,words,memo={},c=0):
    if s in memo:
        return memo[s]
    if s=='':
        return True
    for w in words:
        if s.find(w)==0:
            suffix = s.replace(w,'')
            if canConstruct(suffix,words,memo)== True:
                memo[s]=True
                c+=1

    return c
    
   

# Returns True if we can construct the target string using the words/letters in the list.

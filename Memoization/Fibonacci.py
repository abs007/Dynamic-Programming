def fib(n,memo={}):
    if n not in memo:
        if n<=2:
            return 1
        else:
            memo[n]= fib(n-1,memo)+ fib(n-2,memo)
    return memo[n]

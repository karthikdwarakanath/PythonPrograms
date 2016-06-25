def fibo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1
    else:
        fb = fibo(n-1) + fibo(n-2)
        memo[n] = fb
        return fb


memo = {}
n = 10
print fibo(n)
print memo

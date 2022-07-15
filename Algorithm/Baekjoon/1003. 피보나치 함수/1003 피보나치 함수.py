import sys
input = sys.stdin.readline
def fibonacci(N):
    global dp
    if N == 0 :
        return 0
    elif N == 1 :
        dp[N] = 1
        return 1
    if dp[N] != 0 :
        return dp[N]
    dp[N] = fibonacci(N-1) + fibonacci(N-2)
    return dp[N]

T = int(input())
for _ in range(T):
    dp = [0]*50
    n = int(input())
    if n == 0 :
        print(1,0)
    else :
        fibonacci(n)
        print(dp[n-1],dp[n])

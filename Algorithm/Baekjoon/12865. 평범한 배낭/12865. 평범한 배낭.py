import sys
input = sys.stdin.readline

N,K = map(int,input().split())

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    W,V = map(int,input().split())
    for j in range(1,K+1):
        if W>j :
            dp[i][j] = dp[i-1][j]
        else :
            if j-W>0 :
                dp[i][j] = max(V+dp[i-1][j-W], dp[i-1][j])
            else :
                dp[i][j] = max(V, dp[i-1][j])

print(max(dp[-1]))
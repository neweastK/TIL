N,K = map(int,input().split())

dp = [[0]*200 for _ in range(200)]
dp[0] = [x for x in range(1,201)]


for i in range(1,200):
    dp[i][0] = 1
    for j in range(1,200):
        tmp = 0
        for a in range(i+1):
            tmp+=dp[a][j-1]
        dp[i][j] = tmp+1
print(dp[N-1][K-1]%1000000000)
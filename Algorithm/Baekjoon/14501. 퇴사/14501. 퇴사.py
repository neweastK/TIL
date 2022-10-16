N = int(input())
T = [0]*N
P = [0]*N
dp = [0]*(N+1)
for i in range(N):
    t,p = map(int,input().split())
    T[i] = t
    P[i] = p

for j in range(N-1,-1,-1):
    if j+T[j] > N :
        dp[j] = dp[j+1]
    else :
        dp[j] = max(dp[j+1],P[j]+dp[j+T[j]])

print(dp[0])
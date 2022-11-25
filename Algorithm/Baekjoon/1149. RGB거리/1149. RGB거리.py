N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

dp = [[0]*3 for _ in range(N)]
dp[0] = arr[0][:]

for j in range(1,N):
    dp[j][0] = dp[j-1][1]+arr[j][0] if dp[j-1][1] < dp[j-1][2] else dp[j-1][2]+arr[j][0]
    dp[j][1] = dp[j-1][0]+arr[j][1] if dp[j-1][0] < dp[j-1][2] else dp[j-1][2]+arr[j][1]
    dp[j][2] = dp[j-1][0]+arr[j][2] if dp[j-1][0] < dp[j-1][1] else dp[j-1][1]+arr[j][2]
print(min(dp[N-1]))
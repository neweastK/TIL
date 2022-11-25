N = int(input())
arr = [x for x in map(int,input().split())]
dp = [0]*N
for i in range(len(arr)):
    dp[i] = arr[i]

for j in range(1,N):
    dp[j] = max(dp[j-1]+dp[j],dp[j])

print(max(dp))
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()
arr = list(map(lambda x:x[1],arr))

dp = [1]*N
for i in range(1,N):
    for j in range(0,i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))
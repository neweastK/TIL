import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
arr = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    arr[a][b] = -1
    arr[b][a] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                arr[i][j] = 0
            if arr[i][k] > 0 and arr[k][j]>0:
                arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])
            elif arr[i][k] < 0 and arr[k][j] < 0:
                arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])

for n in range(1,N+1):
    ans = arr[n][1:].count(1e9)
    print(ans)
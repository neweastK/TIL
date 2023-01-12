import sys
input = sys.stdin.readline

N,M = map(int,input().split())
INF = int(1e9)
arr = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            arr[i][j] = 0

for _ in range(M):
    a,b = map(int,input().split())
    arr[a][b] = 1

for k in range(1,N+1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

res = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1, N + 1):
        if arr[i][j] != INF and arr[i][j] != 0:
            res[i]+=1
        if arr[j][i] != INF and arr[j][i] != 0:
            res[i]+=1
ans = res.count(N-1)0
print(ans)
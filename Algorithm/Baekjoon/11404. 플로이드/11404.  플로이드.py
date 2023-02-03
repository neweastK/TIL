import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

INF = int(1e9)
arr = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            arr[i][j] = 0

for _ in range(M):
    a,b,c = map(int,input().split())
    if arr[a][b] != INF:
        arr[a][b] = min(arr[a][b],c)
    else:
        arr[a][b] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == INF:
            arr[i][j] = 0
    print(*arr[i][1:])
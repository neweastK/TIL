import sys
from pprint import pprint

input = sys.stdin.readline

N,M = map(int,input().split())

arr = [[int(1e9)]*(N) for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])

kevin = int(1e9)

for s in range(N):
    if sum(arr[s]) < kevin :
        kevin = sum(arr[s])
        res = s+1

print(res)


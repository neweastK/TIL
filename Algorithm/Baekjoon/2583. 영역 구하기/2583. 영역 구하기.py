import sys
sys.setrecursionlimit(10**6)
from pprint import pprint
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    global c

    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 0 :
            arr[nx][ny] = 1
            c+=1
            dfs(nx,ny)


M,N,K = map(int,input().split())
arr = [[0]*(N) for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2) :
        for j in range(x1,x2):
            arr[i][j] = 1

res = []
for x in range(M):
    for y in range(N):
        if arr[x][y] == 0 :
            arr[x][y] = 1
            c = 1
            dfs(x,y)
            res.append(c)

print(len(res))
print(*sorted(res))
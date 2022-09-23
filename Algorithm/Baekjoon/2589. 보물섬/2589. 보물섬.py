import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(sx,sy):
    visited = [[0]*W for _ in range(L)]
    visited[sx][sy] = 1

    queue = deque([(sx,sy)])
    while queue :
        x,y = queue.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<L and 0<=ny<W and arrs[nx][ny]=="L" and visited[nx][ny] == 0 :
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1
    return visited[x][y]


L,W = map(int,input().split())
arrs = [list(input().rstrip()) for _ in range(L)]

maximum=0
for i in range(L):
    for j in range(W):
        if arrs[i][j] == "L":
            res = bfs(i,j)
            if res>maximum :
                maximum = res
print(maximum-1)
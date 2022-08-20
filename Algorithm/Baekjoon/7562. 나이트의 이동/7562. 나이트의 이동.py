import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    # visited[x][y] = 1
    queue = deque([(x,y)])

    while queue :
        i,j = queue.popleft()
        if [i,j] == target :
            return visited[i][j]

        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]

            if 0<=ni<I and 0<=nj<I and visited[ni][nj]==0:
                visited[ni][nj] = visited[i][j]+1
                queue.append((ni,nj))


di = [-2,-2,-1,-1,1,1,2,2]
dj = [1,-1,2,-2,2,-2,1,-1]

T = int(input())

for _ in range(T):
    I = int(input())
    sx,sy = map(int,input().split())
    target = list(map(int,input().split()))
    visited = [[0]*I for _ in range(I)]
    print(bfs(sx,sy))
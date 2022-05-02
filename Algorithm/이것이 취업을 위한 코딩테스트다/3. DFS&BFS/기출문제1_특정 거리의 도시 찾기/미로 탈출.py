from collections import deque

delta = [(0,1),(0,-1),(1,0),(-1,0)]


def bfs(start):
    queue = deque([start])
    arr[start[0]][start[1]] = 2
    while queue :
        now = queue.popleft()
        for d in delta:
            nx = now[0]+d[0]
            ny = now[1]+d[1]

            if (nx,ny)== (N-1, M-1) :
                return arr[now[0]][now[1]]

            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
                queue.append((nx,ny))
                arr[nx][ny] = arr[now[0]][now[1]]+1

N,M = map(int,input().split())

arr = [list(map(int,input())) for _ in range(N)]
ans = bfs((0,0))
from pprint import pprint
pprint(arr)
print(ans)

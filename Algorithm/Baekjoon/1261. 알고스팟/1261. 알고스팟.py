import sys
from collections import deque
input = sys.stdin.readline


def bfs(sx, sy):
    queue = deque([])
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if maps[nx][ny]:
                    queue.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                else:
                    queue.appendleft((nx, ny))
                    distance[nx][ny] = distance[x][y]


N,M = map(int,input().split())
maps = []
distance = [[0]*N for _ in range(M)]
visit = [[0]*N for _ in range(M)]
for _ in range(M):
    maps.append(list(map(int,input().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

bfs(0,0)
print(distance[M-1][N-1])
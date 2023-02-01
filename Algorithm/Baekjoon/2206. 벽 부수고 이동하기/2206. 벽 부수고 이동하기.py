import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(N)]

visited = [[[0]*M for _ in range(N)] for _ in range(2)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(start_x,start_y):
    queue = deque([(start_x,start_y,0)])
    visited[0][start_x][start_y] = 1

    while queue:
        x,y,crush = queue.popleft()
        if x==N-1 and y==M-1:
            return visited[crush][x][y]

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<N and 0<=ny<M:
                # 탐색 위치가 벽이고 지금까지 안부쉈다면
                if arr[nx][ny] == 1 and crush ==0:
                    if visited[crush][nx][ny] > visited[crush][x][y] + 1 or visited[crush][nx][ny] == 0:
                    # 벽을 부수고 오지 않았다면 (이미 부수고 온 경우 탐색 불가)
                        visited[1][nx][ny] = visited[0][x][y]+1
                        queue.append((nx,ny,1))

                # 탐색 위치가 벽이 아니라면
                elif arr[nx][ny] == 0:
                    if visited[crush][nx][ny]>visited[crush][x][y]+1 or visited[crush][nx][ny]==0:
                    #근데 부수고 왔다면
                        visited[crush][nx][ny] = visited[crush][x][y] + 1
                        queue.append((nx,ny,crush))
    return -1

res = bfs(0,0)
print(res)

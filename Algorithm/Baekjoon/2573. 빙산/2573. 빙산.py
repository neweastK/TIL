import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(N):
    arr.append(list(map(int,input().split())))

def bfs(arr):
    c=0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and check_arr[i][j] == 0 :
                c+=1
                queue = deque([(i,j)])

                while queue :
                    x,y = queue.popleft()
                    check_arr[x][y] = c

                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]

                        if 0<=nx<N and 0<=ny<M and arr[nx][ny]>0 and check_arr[nx][ny] == 0 :
                            check_arr[nx][ny] = c
                            queue.append((nx,ny))
    return c

# 4방향 순회 후 0의 개수만큼 빼기
def melting(x,y):
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if arr[nx][ny] <= 0 :
            new_arr[x][y] -= 1

cnt = 0

while True:
    cnt_zero = 0
    cnt+=1
    new_arr = [x[:] for x in arr[:]]
    check_arr = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 :
                melting(i,j)
            else :
                cnt_zero += 1



    arr = new_arr
    res = bfs(arr)
    if res >= 2:
        print(cnt)
        break
    else :
        if cnt_zero == N*M:
            print(0)
            break


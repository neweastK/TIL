import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(start):
    global cnt
    if len(start) == 0 :
        return
    queue = deque([])
    for x,y in start :
        for d in range(4) :
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0 :
                arr[nx][ny] = 1
                queue.append((nx,ny))
    return queue

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

tomato = deque([])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i,j))
if len(tomato) == 0 :
    print(-1)

else :
    cnt = 0

    while True :
        cnt+=1
        tomato = bfs(tomato)
        if len(tomato) == 0:
            break

    def check_zero():
        tmp = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    tmp += 1
                    return tmp

    res = check_zero()
    if res :
        print(-1)
    else :
        print(cnt-1)
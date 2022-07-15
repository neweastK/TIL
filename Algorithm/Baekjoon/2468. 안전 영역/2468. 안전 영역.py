from collections import deque
import sys

def bfs(si,sj,rain,num):

    queue = deque()
    queue.append([si,sj])
    visited[si][sj] = num

    while queue :
        ci,cj = queue.popleft()

        for d in range(4) :
            ni = ci+dx[d]
            nj = cj+dy[d]

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > rain and visited[ni][nj] == 0 :
                queue.append([ni,nj])
                visited[ni][nj] = num


dx = [0,0,-1,1]
dy = [1,-1,0,0]


input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

res=deque([])
for rain in range(1,101):
    visited = [[0] * N for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and visited[i][j] == 0 :
                num+=1
                bfs(i,j,rain,num)
    res.append(num)
print(max(res))
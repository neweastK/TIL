from collections import deque
import sys
input = sys.stdin.readline

def bfs(queue) :
    maximum = 0
    while queue:
        sh,si,sj = queue.popleft()

        for d in range(6):
            nh = sh+dh[d]
            ni = si+di[d]
            nj = sj+dj[d]

            if 0<=nh<H and 0<=ni<N and 0<=nj<M and maps[nh][ni][nj]==0:
                maps[nh][ni][nj] = 1
                visited[nh][ni][nj] = visited[sh][si][sj] + 1
                queue.append([nh,ni,nj])
                maximum = max(maximum,visited[nh][ni][nj])
    return maximum


M,N,H = map(int,input().split())
maps = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

dh = [1,-1,0,0,0,0]
di = [0,0,1,-1,0,0]
dj = [0,0,0,0,1,-1]

queue = deque([])
E = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if maps[i][j][k] == 1 :
                visited[i][j][k] = 1
                queue.append([i,j,k])
            elif maps[i][j][k] == -1 :
                E += 1

answer = 0
# 모든 토마토의 개수
tomatos = H*M*N-E
# 모든 토마토가 익었다면
if len(queue) == tomatos :
    answer = 0
else :
    total = 0
    res = bfs(queue)
    for a in range(H):
        for b in range(N):
            total += sum(maps[a][b])
    # 다 익었다
    if total+E == tomatos :
        answer = res-1
    else :
        answer = -1

print(answer)
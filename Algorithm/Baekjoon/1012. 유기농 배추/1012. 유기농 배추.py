from collections import deque

def BFS(si,sj):
    global visited
    queue = deque()
    queue.append([si,sj])
    # visited[si][sj] = 1

    while queue :
        ci,cj = queue.popleft()

        for d in range(4):
            ni = ci + dx[d]
            nj = cj + dy[d]

            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:
                queue.append([ni,nj])
                arr[ni][nj] = k


import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())

for _ in range(T) :
    # 가로,세로,배추개수
    M,N,K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K) :
        m,n = map(int,input().split())
        arr[n][m] = 1
    k=2

    for i in range(N) :
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = k
                BFS(i,j)
                k+=1
    print(k-2)
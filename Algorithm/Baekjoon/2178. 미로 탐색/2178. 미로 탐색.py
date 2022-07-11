def BFS(N,M,arr) :
    queue = [(0,0)]
    visited = [[0]*M for _ in range(N)]
    check = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    check[0][0] = 1

    while queue :
        ci,cj = queue.pop(0)
        for d in range(4) :
            ni = ci + dx[d]
            nj = cj + dy[d]

            if 0<=ni<N and 0<=nj<M and visited[ni][nj] != 1 and arr[ni][nj] == 1 :
                visited[ni][nj] = 1
                check[ni][nj] = check[ci][cj] + 1
                queue.append((ni,nj))
    return check



import sys
from pprint import pprint
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [ list(map(int,list(input())[:M])) for _ in range(N) ]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
ans = BFS(N,M,arr)[N-1][M-1]
print(ans)
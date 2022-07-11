def BFS(i,j):
    global arr
    global visited
    queue = [(i,j)]
    visited[i][j] = 1
    cnt=1
    while queue :
        ci,cj = queue.pop(0)
        arr[ci][cj] = 9

        for d in range(4):
            ni = ci + dx[d]
            nj = cj + dy[d]

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] !=1 :
                queue.append((ni,nj))
                visited[ni][nj] = 1
                cnt+=1
    return cnt


import sys
input = sys.stdin.readline

from pprint import pprint
N = int(input())
arr = [ list(map(int,list(input())[:N])) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
res = []
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            res.append(BFS(i,j))

print(len(res))
for k in sorted(res) :
    print(k)
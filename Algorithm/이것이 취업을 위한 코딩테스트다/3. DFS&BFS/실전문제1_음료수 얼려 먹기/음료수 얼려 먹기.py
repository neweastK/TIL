'''
4 5
00110
00011
11111
00000
'''
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
from collections import deque

delta = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(start):
    queue = deque([start])
    while queue :
        now = queue.popleft()
        for d in delta :
            nx = now[0]+d[0]
            ny = now[1]+d[1]

            if 0<=nx<N and 0<=ny<M and ice_form[nx][ny] == 0 :
                queue.append((nx,ny))
                ice_form[nx][ny] = 1

N,M = map(int,input().split())
ice_form = [list(map(int,input())) for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(M):
        if ice_form[i][j] == 0 :
            bfs((i,j))
            cnt +=1

print(cnt)
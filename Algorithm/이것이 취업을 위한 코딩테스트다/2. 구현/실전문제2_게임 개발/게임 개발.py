"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

# 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
dx=[-1,0,1,0]
dy=[0,1,0,-1]



N,M = map(int,input().split())
now = list(map(int,input().split()))
x,y = now[0], now[1]
nd = now[2]
maps = [list(map(int,input().split())) for _ in range(N)]
maps[x][y] = 2
while True :
    for _ in range(4):
        if nd :
            nd -= 1
        else :
            nd = 3
        nx, ny = x+dx[nd], y+dy[nd]

        if maps[nx][ny] == 0 :
            x = nx
            y = ny
            maps[nx][ny] = 2
            break
    else :
        # 정반대 방향 구하는 방법
        nx,ny = x-dx[nd], y-dy[nd]
        if maps[nx][ny] != 1:
            x = nx
            y = ny
            maps[nx][ny] = 2
        else :
            break

cnt=0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2 :
            cnt += 1

print(cnt)

'''
5 5
2 1 0
1 1 1 1 1
1 0 1 1 1
1 0 1 1 1
1 0 1 1 1
1 1 1 1 1
정답 : 3
'''
'''
5 5
1 2 0
1 1 1 1 1
1 1 0 1 1
1 0 1 0 1
1 1 0 1 1
1 1 1 1 1
정답 : 1

5 5
1 2 0
1 1 1 1 1
1 1 0 1 1
1 0 0 0 1
1 1 0 1 1
1 1 1 1 1
정답 : 5

'''
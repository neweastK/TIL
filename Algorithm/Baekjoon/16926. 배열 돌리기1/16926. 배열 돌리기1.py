import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

# 아래 -> 오른쪽 -> 위 -> 왼쪽
dx = [1,0,-1,0]
dy = [0,1,0,-1]
d = 0

for _ in range(R):
    new_maps = [[0]*M for _ in range(N)]
    c = 0
    r = 0
    x,y = (r,r)
    On = N
    Om = M
    # 한번 회전하는 과정
    while On>0 and Om>0:
        while d<4 :
            tmp = maps[x][y]
            x = x+dx[d]
            y = y+dy[d]
            new_maps[x][y] = tmp
            c+=1
            # 좌,우 이동일 경우
            if d%2 :
                if c == Om-1 :
                    d+=1
                    c=0
            else :
                if c == On-1 :
                    d+=1
                    c=0
        r+=1
        x,y=(r,r)
        d=0
        On=On-2
        Om=Om-2
    maps = [new_map[:] for new_map in new_maps[:]]

for map in maps :
    print(*map)
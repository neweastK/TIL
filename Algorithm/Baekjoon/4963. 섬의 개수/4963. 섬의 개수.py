dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
def make_island(x,y,cnt):
    global maps
    for d in range(8):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<h and 0<=ny<w and maps[nx][ny] == 1:
            maps[nx][ny] = cnt
            make_island(nx,ny,cnt)


while True :
    w,h = map(int,input().split())
    if (w,h) == (0,0) :
        break

    maps = [list(map(int,input().split())) for _ in range(h)]
    cnt=2
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                make_island(i,j,cnt)
                cnt+=1

    print(cnt-2)

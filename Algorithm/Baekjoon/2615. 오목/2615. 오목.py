def check_omok(si,sj,color):
    for delta in range(4):
        cnt = 1
        for d in range(2):
            x, y = si, sj
            while True :
                ni = x+dx[delta][d]
                nj = y+dy[delta][d]

                if 0<=ni<19 and 0<=nj<19 and maps[ni][nj] == color:
                    cnt+=1
                    x = ni
                    y = nj
                else :
                    break

        if cnt == 5:
            return True

    return False



dx = [(0,0),(1,-1),(1,-1),(-1,1)]
dy = [(1,-1),(0,0),(1,-1),(1,-1)]
maps = [list(map(int,input().split())) for _ in range(19)]


for j in range(19):
    for i in range(19):
        if maps[i][j] != 0:
            if check_omok(i,j,maps[i][j]):
                print(maps[i][j])
                print(i+1,j+1)
                quit()

print(0)

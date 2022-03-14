import sys
sys.stdin = open("input.txt")
from pprint import pprint


T = int(input())

for tc in range(T) :

    N, M, K = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    groups = [list(map(int,input().split())) for _ in range(K)]

    for group in groups:
        arr[group[0]][group[1]] = [group[2], group[3]]

    cd = {1:2, 2:1, 3:4, 4:3}
    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]

    for _ in range(M):
        new_arr = [[0] * N for _ in range(N)]
        tmp_arr = [[0]*N for _ in range(N)]
        for i in range(N) :
            for j in range(N) :
                val = arr[i][j]
                if val :
                    nx = i + dx[val[1]]
                    ny = j + dy[val[1]]
                    if nx==0 or nx==N-1 or ny==0 or ny==N-1 :
                        new_arr[nx][ny] = [val[0]//2, cd.get(val[1])]
                    elif new_arr[nx][ny] == 0  :
                        new_arr[nx][ny] = [val[0],val[1]]
                    else :
                        if new_arr[nx][ny][0] > val[0] :
                            tmp_arr[nx][ny] += val[0]
                        else :
                            tmp_arr[nx][ny] += new_arr[nx][ny][0]
                            new_arr[nx][ny] = [val[0],val[1]]

                        # nd = new_arr[nx][ny][1] if new_arr[nx][ny][0] > val[0] else val[1]
                        # new_arr[nx][ny] = [new_arr[nx][ny][0] + val[0], nd]
        for tmp_i in range(N) :
            for tmp_j in range(N) :
                if tmp_arr[tmp_i][tmp_j] :
                    new_arr[tmp_i][tmp_j][0] += tmp_arr[tmp_i][tmp_j]
        arr = [new[:] for new in new_arr]

    res = 0
    for ni in range(N) :
        for nj in range(N) :
            if new_arr[ni][nj] :
                res += new_arr[ni][nj][0]

    print(f'#{tc+1} {res}')
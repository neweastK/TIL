import sys
from itertools import combinations
input = sys.stdin.readline

# 거리 측정
def distance(x1,y1,x2,y2):
    distance = abs(x1-x2)+abs(y1-y2)
    return distance

N,M,D = map(int,input().split())

arr_original = [list(map(int,input().split())) for _ in range(N)]
enemies = []
# 성과 궁수가 위치할 공간
arr_original.append([0]*M)
arrows = list(combinations(range(M),3))
ans = 0
for arrow in arrows:
    tmp_cnt = 1
    arr = [x[:] for x in arr_original]
    cnt = 0
    while tmp_cnt:
        target = []
        for a in arrow:
            player = [N,a]
            player_dist = 999999
            tmp = []
            for i in range(N):
                for j in range(M):
                    if arr[i][j] == 1:
                        # 현재 궁수와 적의 거리
                        dist = distance(N,a,i,j)

                        if dist<player_dist and dist<=D:
                            player_dist = dist
                            tmp = [i,j]
                        elif dist==player_dist:
                            if tmp[1]>j:
                                tmp = [i,j]

            if tmp:
                target.append(tmp)

        tmp_cnt = 0
        for ni in range(N-1,-1,-1):
            for nj in range(M-1,-1,-1):
                if [ni,nj] in target:
                    arr[ni][nj] = 0
                    cnt += 1

                if arr[ni][nj] == 1:
                    arr[ni+1][nj] = 1
                    arr[ni][nj] = 0
                    tmp_cnt += 1

    if ans<cnt:
        ans = cnt
print(ans)






import sys
input = sys.stdin.readline
from collections import deque

N,M,K = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

fireballs = deque([list(map(int,input().split())) for _ in range(M)])

for _ in range(K):
    visited = [[[0,0,0,[]] for _ in range(N)] for _ in range(N)]
    while fireballs:
        r,c,m,s,d = fireballs.popleft()
        # 1. 새로운 위치 찾기
        nr = ((r-1)+s*dx[d])%N
        nc = ((c-1)+s*dy[d])%N

        # 방문처리
        visited[nr][nc][0] += 1
        visited[nr][nc][1] += m
        visited[nr][nc][2] += s
        visited[nr][nc][3].append(d)

    # fireball 나누기
    for i in range(N):
        for j in range(N):
            now = visited[i][j]
            # 해당 위치에 하나만 있는 경우
            if now[0] == 1:
                fireballs.append([i+1,j+1,now[1],now[2],now[3][0]])

            # 해당 위치에 파이어볼이 2개 이상있는 경우
            elif now[0] > 1:
                nm = now[1]//5
                if nm == 0:
                    continue
                ns = now[2]//now[0]
                tmp = [0]*now[0]
                nd = [0,2,4,6]
                # 전부다 짝수인지 홀수인지 판단
                for d in range(now[0]):
                    tmp[d] = now[3][d]%2
                    if d>=1:
                        # 하나라도 다르면
                        if tmp[d-1] != tmp[d]:
                            nd = [1,3,5,7]
                            break
                # 4개로 나누기
                for new in range(4):
                    fireballs.append([i+1,j+1,nm,ns,nd[new]])


res = sum(list(map(lambda x:x[2],fireballs)))
print(res)
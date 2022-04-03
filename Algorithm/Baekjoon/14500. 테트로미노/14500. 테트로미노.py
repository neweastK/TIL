from pprint import pprint

# 한번의 순회 과정은 모든 사각형 네개의 합을 구하고 그 중 최댓값을 구한다
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def DFS(n,arr_check,x,y,total) :
    if n == 4 :
        res.append(total)
    else :
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<M and arr_check[nx][ny] == 0 :
                arr_check[nx][ny] = 1
                DFS(n+1,arr_check,nx,ny,total+arr[nx][ny])
                arr_check[nx][ny] = 0


# 십자가 모양으로 더하기
def cross_total(x,y) :
    res_cross = 0
    for d in range(4) :
        total_cross = arr[x][y]
        for dd in range(d,d+3):
            nx = x+dx[dd%4]
            ny = y+dy[dd%4]
            if 0 <= nx < N and 0 <= ny < M :
                total_cross += arr[nx][ny]

        if res_cross < total_cross :
            res_cross = total_cross
    return res_cross

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
arr_check = [[0] * M for _ in range(N)]

ans=0
res = []

for i in range(N):
    for j in range(M):
        arr_check[i][j] = 1
        DFS(1,arr_check,i,j,arr[i][j])
        arr_check[i][j] = 0
        cross_max_res=cross_total(i,j)
        res.append(cross_max_res)
print(max(res))
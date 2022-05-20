def dfs(arr,x,y,base):
    global cnt
    stack = [(x,y)]

    while stack :
        x,y = stack.pop()
        arr[x][y] = cnt
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == base :
                stack.append((nx,ny))

    cnt += 1
    return cnt

from pprint import pprint
N = int(input())
arr = [list(input()) for _ in range(N)]
arr_second = [ item[:] for item in arr ]
# 글자의 실제 자리수를 표시할 리스트

dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0
for i in range(N):
    for j in range(N):
        if type(arr[i][j]) == str :
            base = arr[i][j]
            res = dfs(arr,i,j,base)

        if arr_second[i][j] == "G" :
            arr_second[i][j] = "R"

cnt = 0
for k in range(N):
    for l in range(N):
        if type(arr_second[k][l]) == str :
            new_base = arr_second[k][l]
            new_res = dfs(arr_second,k,l,new_base)

print(res, new_res)

import sys
input = sys.stdin.readline

def dfs(c,si,sj):
    global check
    global res

    if c>res :
        res = c

    for d in range(4):
        ni = si+dx[d]
        nj = sj+dy[d]
        if 0<=ni<R and 0<=nj<C and check[arr[ni][nj]] == 0 :
            check[arr[ni][nj]] = 1
            dfs(c+1,ni,nj)
            check[arr[ni][nj]] = 0


R,C = map(int,input().split())
arr = [list(map(lambda x: ord(x)-65,input().rstrip())) for _ in range(R)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

res = 0
check = [0]*26
check[arr[0][0]] = 1
c = 1
dfs(c,0,0)
print(res)
import sys
input = sys.stdin.readline

def dfs(x,y,dist):
    print(visited)
    global res
    if maps[x][y] == -1 :
        res = "HaruHaru"
        return
    for d in range(2):
        nx = x+dx[d]*dist
        ny = y+dy[d]*dist

        if 0<=nx<N and 0<=ny<N and (nx,ny) not in visited :
            visited.append((nx,ny))
            dfs(nx,ny,maps[nx][ny])
            visited.pop()


N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0]
dy = [0,1]
visited = [(0,0)]
res = "Hing"
dfs(0,0,maps[0][0])
print(res)
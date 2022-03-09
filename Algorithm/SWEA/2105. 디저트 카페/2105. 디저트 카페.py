import sys
sys.stdin = open("input.txt")

T = int(input())
cnt = 0
def dfs(x,y,visited) :
    global cnt
    delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for d in delta :
        nx = x+d[0]
        ny = y+d[1]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in visited:
            cnt+=1
            dfs(nx,ny,visited)


for tc in range(T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    delta = [[1,1],[1,-1],[-1,-1],[-1,1]]
    cnt = -1
    for i in range(N) :
        for j in range(N) :
            visited = []
            x = i
            y = j
            visited.append(arr[x][y])






            for d in delta :
                while True :
                    x = x + d[0]
                    y = y + d[1]
                    if 0<=x<N and 0<=y<N and arr[x][y] not in visited :
                        visited.append(arr[x][y])
                    elif x==i and y==j :
                        tmp = len(visited)
                        if tmp >= 4 and cnt<tmp :
                            cnt = tmp
                        break
                    else :
                        x = x - d[0]
                        y = y - d[1]
                        break

    print(cnt)

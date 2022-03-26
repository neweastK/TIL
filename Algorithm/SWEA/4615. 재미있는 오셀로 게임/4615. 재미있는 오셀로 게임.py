import sys
sys.stdin = open("input.txt")


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def othello(x,y,c,dx,dy) :
    global arr
    arr[x][y] = c #해당 위치에 자신의 돌(c) 놓기

    for d in range(len(dx)) : #8방향 다 돌기
        nx = x+dx[d] #먼저 한칸씩 살펴보기
        ny = y+dy[d]
        tmp = []
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 3-c : #범위에서 벗어나지 않고 상대방 돌이라면
            while 0<=nx<N and 0<=ny<N : #범위 벗어나지 않도록
                if arr[nx][ny] == 0 : #빈칸이면 다 초기화 (처음에는 있을 수 없음 위의 if문 때문에)
                    break
                elif arr[nx][ny] == c : #만약 자신의 돌을 만나면 (처음에는 있을 수 없음 위의 if문 때문에)
                    for tx,ty in tmp : #지금까지 담아온 위치들을 다 자신의 색으로 바꿔주기
                        arr[tx][ty] = c
                    break
                else : #다른 사람 돌이면
                    tmp.append([nx, ny])
                    nx = nx + dx[d] #한칸 더 이동
                    ny = ny + dy[d]


T = int(input())

for tc in range(T):
    N,M = map(int,input().split()) #N은 보드 넓이, M은 돌을 놓는 횟수

    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = 2

    for _ in range(M) :
        y,x,c = map(int,input().split())
        othello(x-1,y-1,c,dx,dy)

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 :
                black += 1
            elif arr[i][j] == 2 :
                white += 1

    print(f"#{tc+1} {black} {white}")
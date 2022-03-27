def maze(start, arr):
    stack = [start]

    while stack:
        tmp = stack[-1]
        x = tmp[0]
        y = tmp[1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 4
                stack.append((nx, ny))
                break
            elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 3:
                return 1
        else:
            stack.pop()

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 :
                start = (i,j)

    # 델타
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    result = 1 if maze(start,arr) == 1 else 0
    print(f"#{tc+1} {result}")

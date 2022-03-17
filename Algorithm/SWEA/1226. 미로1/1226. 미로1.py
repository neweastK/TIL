import sys
sys.stdin = open("input.txt")

def maze(arr):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    stack = []
    visited = []
    stack.append([1,1])

    while stack :
        loc_x, loc_y = stack[-1]
        for d in range(4):
            nx = loc_x + dx[d]
            ny = loc_y + dy[d]

            if 0<=nx<16 and 0<=ny<16 and arr[nx][ny] != 1  and [nx,ny] not in visited:
                if arr[nx][ny] == 3 :
                    return 1
                stack.append([nx,ny])
                visited.append([nx, ny])
                break


        else :
            stack.pop()


for _ in range(10) :
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(16)]

    result = maze(arr)
    if result :
        print(f"#{tc} {result}")
    else :
        print(f"#{tc} 0")
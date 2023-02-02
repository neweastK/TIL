import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

move = list(map(int,input().split()))

delta = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
dice = [0]*7

top = 1
bottom = 6

def dice_moving(direction):
    tmp_dice = dice[:]
    # 동쪽 이동
    if direction == 1:
        dice[3],dice[6],dice[4],dice[1] = tmp_dice[1],tmp_dice[3],tmp_dice[6],tmp_dice[4]

    # 서쪽 이동
    elif direction == 2:
        dice[1],dice[3],dice[6],dice[4] = tmp_dice[3], tmp_dice[6],tmp_dice[4],tmp_dice[1]

    # 북쪽 이동
    elif direction == 3:
        dice[2],dice[5],dice[6],dice[1] = tmp_dice[1],tmp_dice[6],tmp_dice[2],tmp_dice[5]

    # 남쪽 이동
    else:
        dice[1],dice[6],dice[2],dice[5] = tmp_dice[2],tmp_dice[5],tmp_dice[6],tmp_dice[1]

for k in move:
    nx,ny = x+delta[k][0],y+delta[k][1]

    if 0<=nx<N and 0<=ny<M:
        dice_moving(k)
        map_value = arr[nx][ny]
        if map_value == 0:
            arr[nx][ny] = dice[bottom]
        else:
            dice[bottom] = map_value
            arr[nx][ny] = 0

        x,y = nx,ny
        print(dice[top])

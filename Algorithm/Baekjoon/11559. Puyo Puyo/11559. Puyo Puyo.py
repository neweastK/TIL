from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx,sy):
    remove_list=[]
    queue = deque([])
    queue.append((sx,sy))
    visited[sx][sy] = 1
    remove_list.append((sx,sy))

    while queue :
        x,y = queue.popleft()
        target = new_maps[x][y]

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<6 and 0<=ny<12 and visited[nx][ny] == 0 :
                if new_maps[nx][ny] == target :
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    remove_list.append((nx,ny))
    # print(remove_list)
    if len(remove_list) >= 4 :
        total_remove.extend(remove_list)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

maps = [list(map(str,input().rstrip())) for _ in range(12)]
new_maps = []
for j in range(5,-1,-1):
    tmp = deque([])
    for i in range(12) :
        tmp.append(maps[i][j])
    new_maps.append(tmp)

cnt = 0
while True :
    visited = [[0]*12 for _ in range(6)]
    total_remove = []

    for a in range(6):
        for b in range(12):
            if new_maps[a][b] != "." and visited[a][b] == 0 :
                bfs(a,b)

    # from pprint import pprint
    # pprint(new_maps)
    # pprint(visited)
    # print(total_remove)

    # 한번에 지워줘야함. 지우고 나서 다시 반복 돌리면 위치가 바뀌어버림
    if total_remove :
        for item_x,item_y in total_remove :
            new_maps[item_x][item_y] = "delete"

        for item_x,item_y in total_remove :
            new_maps[item_x].remove("delete")
            new_maps[item_x].appendleft('.')
        cnt += 1
    else :
        break
    # pprint(new_maps)
print(cnt)
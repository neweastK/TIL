from collections import deque

delta=[(0,1),(0,-1),(1,0),(-1,0)]

def BFS(x,y,time,cheese):
    global res
    if cheese<0 :
        result.append(time-1)
        result.append(res)
        return

    else:
        q = [(x,y)]
        remove_list=[]
        queue=deque(q)
        visited=[]
        while queue :
            cx,cy=queue.popleft()
            for d in range(4):
                nx = cx+delta[d][0]
                ny = cy+delta[d][1]

                if 0<=nx<H and 0<=ny<W and arr[nx][ny] == 1 :
                    remove_list.append((nx,ny))
                elif 0<=nx<H and 0<=ny<W and arr[nx][ny]==0 and (nx,ny) not in visited :
                    visited.append((nx,ny))
                    queue.append((nx,ny))

        if remove_list:
            res = len(set(remove_list))
            for rx,ry in remove_list :
                arr[rx][ry] = 0
        else :
            cheese = -1
        BFS(1,1,time+1,cheese)



from pprint import pprint
H,W = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(H)]
remove_list = [(0,0)]
res=0
result=[]
BFS(1,1,0,0)
print(result[0])
print(result[1])

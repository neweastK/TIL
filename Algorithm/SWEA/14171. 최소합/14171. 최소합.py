import sys
sys.stdin = open("input.txt")

dx=[1,0]
dy=[0,1]

# def DFS(x,y,total):
#     global res
#     if (x,y) == (N-1,N-1) :
#         total+=arr[x][y]
#         res.append(total)
#         return
#     else :
#         total+=arr[x][y]
#         for d in range(2):
#             nx = x+dx[d]
#             ny = y+dy[d]
#             if 0<=nx<N and 0<=ny<N :
#                 DFS(nx,ny,total)

def DFS(x,y,total):
    global res
    if (x,y) == (N-1,N-1) :
        total+=arr[x][y]
        res.append(total)
        return
    else :
        for d in range(2):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N :
                DFS(nx,ny,total+arr[x][y])


T = int(input())
for tc in range(T):

    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    res=[]
    DFS(0,0,0)
    print(f"#{tc+1} {min(res)}")


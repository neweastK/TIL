# def DFS(n,tmp,lsts) :
#     global result
#     if n == 7 :
#         result.append("".join(map(str,tmp)))
#     else :
#         for lst in lsts :
#             DFS(n+1,tmp+[lst],lsts)

#
# numbers = []
# for _ in range(4) :
#     numbers += list(map(int,input().split()))
#
# print(set(numbers))
# result = []
# DFS(0,[],set(numbers))
# print(result)
import sys
sys.stdin = open("input.txt")

dx = [1,-1,0,0]
dy = [0,0,-1,1]
def DFS(x,y,tmp):
    global result
    N=4
    tmp.append(arr[x][y])
    if len(tmp) == 7 :
        result.append("".join(map(str,tmp)))
        return
    else :
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N :
                # DFS(nx,ny,tmp+[arr[nx][ny]])
                DFS(nx, ny, tmp)

T = int(input())
for tc in range(T):
    arr = [list(map(int,input().split())) for _ in range(4)]
    result=[]
    for i in range(4) :
        for j in range(4) :
            DFS(i,j,[])
    print(f"#{tc+1} {len(set(result))}")
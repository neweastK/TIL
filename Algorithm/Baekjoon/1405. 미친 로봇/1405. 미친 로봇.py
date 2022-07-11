import sys
from collections import deque
input = sys.stdin.readline
# 확률 구하기
def percent(arr):
    tmp = 1
    for dic in arr :
        tmp *= per[dic]
    return tmp

# 단순한 경로의 경우
def dfs(x,y,num):
    global success
    global visited
    visited.append((x,y))
    # 성공 조건 (n번만큼 돌 동안 이전 위치에 안갔다면)
    if num >= n :
        tmp = percent(stack)
        success+=tmp
        visited.pop()
        stack.pop()
        return

    else :
        for k,d in delta.items():
            nx = x+d[0]
            ny = y+d[1]
            if (nx,ny) in visited:
                continue
            # 확률이 0이면 끊자
            if per[k] == 0:
                continue
            else :
                stack.append(k)
                dfs(nx,ny,num+1)
        else :
            visited.pop()
            try :
                stack.pop()
            except:
                pass

n,*p = list(map(int,input().split()))
per = {'E':p[0]*0.01,'W':p[1]*0.01,'S':p[2]*0.01,'N':p[3]*0.01}
delta = {'E':(1,0),'W':(-1,0),'S':(0,1),'N':(0,-1)}
success = 0
stack = deque()
visited = deque()

dfs(0,0,0)
print(success)

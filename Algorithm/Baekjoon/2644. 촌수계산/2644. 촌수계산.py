import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,end):
    visited = [0]*(N+1)
    queue = deque([start])
    dist = [0] * (N + 1)
    dist[start] = 0

    while queue:
        now = queue.popleft()

        if now == end :
            return dist

        for i in arr[now]:
            if visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
                dist[i] = dist[now]+1
    return dist

N = int(input())
start,end = list(map(int,input().split()))
M = int(input())

# 부모 노드를 기록할 리스트
arr = [deque([]) for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

res = bfs(start,end)

if res[end] :
    print(res[end])
else :
    print(-1)
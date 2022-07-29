import sys
from collections import deque
input = sys.stdin.readline

def dfs(V,visited):
    visited.append(V)

    for now in arr[V]:
        if now not in visited :
            dfs(now,visited)
    return visited


def bfs(V):
    queue = deque([V])
    visited = [V]

    while queue :
        now = queue.popleft()
        for v in arr[now]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

N, M, V = map(int,input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,N+1):
    arr[i].sort()


visited = []
print(*dfs(V,visited))
print(*bfs(V))
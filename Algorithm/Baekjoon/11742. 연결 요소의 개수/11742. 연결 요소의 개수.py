import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([])
    queue.append(start)
    visited[start] = 1

    while queue :
        now = queue.popleft()
        for c in graph[now]:
            if visited[c] == 0 :
                queue.append(c)
                visited[c] = 1

N,M = map(int,input().split())
graph = [deque([]) for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

num = 0
for v in range(1,N+1) :
    if visited[v] == 0 :
        num+=1
        bfs(v)

print(num)
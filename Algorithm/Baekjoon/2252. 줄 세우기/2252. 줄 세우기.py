import sys
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

indegree = [0]*(N+1)
queue = deque()

answer = []
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    answer.append(now)
    for j in graph[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)

print(*answer)
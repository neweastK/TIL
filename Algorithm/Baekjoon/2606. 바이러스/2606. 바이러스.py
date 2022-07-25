import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
queue = deque([1])

for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

while queue :
    now = queue.popleft()
    if visited[now] == 0 :
        queue.extend(arr[now])
        visited[now] = 1

print(sum(visited)-1)

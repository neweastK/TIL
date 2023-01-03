import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if visited[i] == visited[now]:
                return False
            elif visited[i] == 0:
                queue.append(i)
                visited[i] = -visited[now]
    return True

K = int(input())
for _ in range(K):
    V,E = map(int,input().split())

    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)

    visited = [0]*(V+1)
    visited[0] = 1
    start_num = 1
    while True:
        res = bfs(start_num)
        if 0 in visited and res:
            start_num = visited.index(0)
            continue
        break

    if res:
        print("YES")
    else:
        print("NO")
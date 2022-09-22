N = int(input())
maps = [[]*(N+1) for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)
connections = [[] for _ in range(N+1)]
visited = [False]*(N+1)
stack = [1]
visited[1] = True
# 1번 노드부터 자식노드 찾기
while stack :
    i = stack.pop()
    for m in maps[i]:
        if visited[m] == False :
            visited[m] = True
            # m번 노드의 부모노드는
            connections[m] = i
            stack.append(m)

for connection in connections[2:]:
    print(connection)
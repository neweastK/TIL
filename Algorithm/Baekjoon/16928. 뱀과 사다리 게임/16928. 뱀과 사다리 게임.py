from collections import deque

def bfs(start):
    queue = deque([])
    queue.append(start)

    while queue:
        now = queue.popleft()

        for d in range(1,7):
            new = now+d

            if 1<=new<101:
                if count[new] >= count[now]+1 or count[new] == 0:
                    count[new] = count[now]+1

                    if maps[new] == 0:
                        queue.append(new)
                    else:
                        if count[maps[new]] >= count[now]+1 or count[maps[new]]==0:
                            count[maps[new]] = count[now]+1
                            queue.append(maps[new])

N,M = map(int,input().split())
maps = [0]*101
count = [0]*101
for _ in range(N):
    a,b = map(int,input().split())
    maps[a] = b

for _ in range(M):
    a,b = map(int,input().split())
    maps[a] = b

bfs(1)
print(count[100])
def dfs(start,cnt,visited):
    global res
    if cnt >= 4:
        res = 1
        return
    else:
        # start에 연결된 애들
        for node in maps[start]:
            # print(node,start,"node와 start",visited)
            if node not in visited:
                dfs(node,cnt+1,visited+[node])

N,M = map(int,input().split())
maps = [[] for _ in range(N)]
res = 0
for _ in range(M):
    a,b = map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)

for i in range(N):
    dfs(i,0,[i])
    if res == 1:
        break
print(res)
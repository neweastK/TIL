def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
maps = []
edges = []
parent = [0]*N

for i in range(N):
    maps.append(list(map(float,input().split())))
    parent[i] = i

all_edge = list(combinations(range(N),2))
for edge in all_edge:
    a,b = edge
    distance = math.sqrt((maps[a][0]-maps[b][0])**2 + (maps[a][1]-maps[b][1])**2)
    edges.append((distance,a,b))

edges.sort()
res = 0
for edge in edges:
    cost,a,b = edge
    if find(a) != find(b):
        union(a,b)
        res += cost

print(res)
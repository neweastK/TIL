import sys
input = sys.stdin.readline

def find_parents(x):
    if x!=parents[x]:
        parents[x] = find_parents(parents[x])
        return parents[x]
    return x

def union(a,b):
    a = find_parents(a)
    b = find_parents(b)

    if a>b:
        parents[a] = b
    else:
        parents[b] = a

N = int(input())

planets = [list(map(int,input().split())) for _ in range(N)]
edges = []
x = []
y = []
z = []

for i in range(len(planets)):
    x.append((planets[i][0],i))
    y.append((planets[i][1],i))
    z.append((planets[i][2],i))

x.sort()
y.sort()
z.sort()

for j in range(1,N):
    edges.append((x[j][0]-x[j-1][0],x[j-1][1],x[j][1]))
    edges.append((y[j][0]-y[j-1][0],y[j-1][1],y[j][1]))
    edges.append((z[j][0]-z[j-1][0],z[j-1][1],z[j][1]))


parents = [0]*N
for p in range(N):
    parents[p] = p

res = 0

edges.sort()
for edge in edges:
    cost,a,b = edge
    # 연결되어있지 않다면
    if find_parents(a) != find_parents(b):
        # 연결해주고
        union(a,b)
        res += cost

print(res)

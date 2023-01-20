dpaximport sys
import math
input = sys.stdin.readline

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
        return parents[x]
    return x

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a>b:
        parents[a] = b
    else:
        parents[b] = a

N,M = map(int,input().split())
parents = [0]*(N+1)
locations = [(0,0)]*(N+1)
for i in range(1,N+1):
    parents[i] = i
    locations[i] = list(map(int,input().split()))

for _ in range(M):
    a,b = map(int,input().split())
    if find_parent(a) != find_parent(b):
        union(a,b)

edges = []
for n in range(1,N+1):
    for i in range(n,N+1):
            cost = (locations[n][0]-locations[i][0])**2 + (locations[n][1]-locations[i][1])**2
            edges.append((n,i,cost**0.5))

edges.sort(key=lambda x:x[-1])
res = 0
for edge in edges:
    a,b,cost = edge
    if find_parent(a) != find_parent(b):
        union(a,b)
        res+=cost
ans = round(res,2)
print(f"{ans:.2f}")
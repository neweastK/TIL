import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)

    if a>b:
        parent[a] = b
    elif a<b:
        parent[b] = a
    else:
        return True

N,M = map(int,input().split())

parent = [0]*N
for i in range(N):
    parent[i] = i

for j in range(M):
    a,b = map(int,input().split())
    tmp = union(a,b)
    if tmp:
        print(j+1)
        break

else:
    print(0)

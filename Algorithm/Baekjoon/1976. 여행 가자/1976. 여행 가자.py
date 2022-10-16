import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x:
        return find(parent[x])
    else :
        return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b :
        parent[b] = a
    else :
        parent[a] = b

N = int(input())
M = int(input())

parent = [0]*(N+1)

for i in range(0,N+1):
    parent[i] = i

for j in range(1,N+1):
    tmp = list(map(int,input().split()))
    for k in range(N):
        if tmp[k] == 1 :
            union(j,k+1)

plans = list(map(int,input().split()))
res = 1
for l in range(1,len(plans)):
    ans1 = find(plans[l-1])
    ans2 = find(plans[l])
    if ans1 != ans2 :
        res=0
        break
if res :
    print("YES")
else :
    print("NO")
import sys
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue :
        dist, target = heapq.heappop(queue)

        if dist > distance[target] :
            continue
        else :
            for i in arr[target] :
                cost = dist + i[1]
                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(queue,(cost,i[0]))



input = sys.stdin.readline
INF = int(1e9)
N,M,K,X = map(int,input().split())

arr = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append((b,1))

dijkstra(X)
res = []
for i in range(1,N+1):
    if distance[i] == K :
        res.append(i)

if res :
    for j in res :
        print(j)
else :
    print(-1)
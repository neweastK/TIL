import heapq
import sys

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue,(0,start))
    while queue :
        dist, target = heapq.heappop(queue)

        if distance[target] < dist :
            continue

        for i in graph[target] :
            cost = dist + i[0]
            if distance[i[1]] > cost :
                distance[i[1]] = cost
                heapq.heappush(queue,(cost,i[1]))

input = sys.stdin.readline
V,E = map(int,input().split())
K = int(input())
INF = int(1e9)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

distance = [INF]*(V+1)
dijkstra(K)

for v in range(1,V+1) :
    res = distance[v]
    if res == INF :
        print('INF')
    else :
        print(res)
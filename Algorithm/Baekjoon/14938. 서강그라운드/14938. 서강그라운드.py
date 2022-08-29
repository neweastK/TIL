import sys
import heapq
input = sys.stdin.readline

def dijkstra(start) :
    queue = []
    heapq.heappush(queue, (start,0))
    # 출발지에서 출발지까지는 거리가 0
    distance[start] = 0

    while queue :
    # 출발지에서 가장 가까운 노드와 거리
        target,dist = heapq.heappop(queue)

        if distance[target] < dist :
            continue

        for i in graph[target] :
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0],cost))

n,m,r = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    heapq.heappush(graph[a],(b,l))
    heapq.heappush(graph[b],(a, l))

res = 0
for area in range(1,n+1):
    distance = [int(1e9)]*(n+1)
    dijkstra(area)
    tmp = 0
    for d in range(1,n+1):
        if distance[d]<=m:
            tmp += items[d-1]

    if res < tmp :
        res = tmp

print(res)
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue :
        dist, target = heapq.heappop(queue)

        if dist > distance[target]:
            continue

        else:
            for i in graph[target]:
                cost = dist+i[0]
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(queue,(cost,i[1]))

T = int(input())
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((s,a))


    distance = [int(1e9)]*(n+1)
    dijkstra(c)
    res = [x for x in distance if x < 1e9]
    print(len(res),max(res))
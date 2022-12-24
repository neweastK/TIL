import heapq


def dijkstra(start):
    queue = [(start, 0)]
    distance[start] = 0

    while queue:
        target, dist = heapq.heappop(queue)

        if dist > distance[target]:
            continue

        for i in graph[target]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))


N, K = map(int, input().split())

distance = [1e9] * 200001
graph = [[] for _ in range(200001)]
for i in range(len(graph) // 2 + 1):
    tmp = [(i - 1, 1), (i + 1, 1), (2 * i, 0)]
    graph[i] = tmp
dijkstra(N)
print(distance[K])

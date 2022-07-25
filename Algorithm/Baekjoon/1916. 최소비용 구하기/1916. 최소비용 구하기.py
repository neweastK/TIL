import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 0번 노드가 없다면 n+1로 설정 (편리성을 위해)
# graph에는 (목적지, 비용)의 튜플이 들어감
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start,target = map(int,input().split())

# start 노드에서 각 index번 노드까지의 최소 거리
distance = [int(1e9)] * (N+1)

def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    # start 노드에서 start노드. 즉, 본인까지의 거리는 0
    distance[start] = 0

    while queue:
        dist, target = heapq.heappop(queue)

        if distance[target] < dist:
            continue

        # start노드에서 출발해 target노드를 거쳐 가는 것이 더 짧은지 비교
        for i in graph[target]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

djikstra(start)
print(distance[target])
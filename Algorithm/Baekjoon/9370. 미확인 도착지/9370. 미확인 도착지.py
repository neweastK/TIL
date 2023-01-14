import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    distance = [INF]*(N+1)
    queue = [(start,0)]
    distance[start] = 0

    while queue:
        now,dist = heapq.heappop(queue)

        if dist>distance[now]:
            continue
        else:
            for i in maps[now]:
                cost = dist+i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue,[i[0],cost])
    return distance

K = int(input())
for k in range(K):

    # 교차로, 도로, 목적지 후보 개수
    N,M,T = map(int,input().split())

    # 시작점, 교차로 지점(G와 H 사이 도로를 무조건 지나감
    S,G,H = map(int,input().split())

    INF = int(1e9)
    maps = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b,d = map(int,input().split())
        maps[a].append([b,d])
        maps[b].append([a,d])

    dist_start = dijkstra(S)
    dist_G = dijkstra(G)
    dist_H = dijkstra(H)

    ans = []
    for _ in range(T):
        t = int(input())
        dist_ST = dist_start[t]
        dist_SGHT = dist_start[G] + dist_G[H] + dist_H[t]
        dist_SHGT = dist_start[H] + dist_H[G] + dist_G[t]

        if dist_ST == dist_SGHT or dist_ST == dist_SHGT:
            ans.append(t)
    ans.sort()
    print(*ans)
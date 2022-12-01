import heapq

def djikstra(start):
    tmp_distance[start] = 0
    queue = [(start,0)]

    while queue:
        node,dist = heapq.heappop(queue)

        if dist > tmp_distance[node]:
            continue

        else:
            for i in graph[node]:
                cost = dist+i[1]
                if cost < tmp_distance[i[0]]:
                    tmp_distance[i[0]] = cost
                    heapq.heappush(queue,(i[0],cost))


T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    k = int(input())
    starts = list(map(int,input().split()))
    distance = []
    for start in starts:
        tmp_distance = [(1e9)]*(N+1)
        djikstra(start)
        distance.append(tmp_distance)

    res = 999999999
    answer = 0
    for i in range(1,N+1):
        tmp = 0
        for j in range(k):
            tmp += distance[j][i]
        if res>tmp:
            res = tmp
            answer = i
    print(answer)
# #최단거리 구하기
# def shortest_distance(n,m,k):
#     for i in arr[n] :
#         distance[m][i] = k
#         shortest_distance(i,m,k+1)


from pprint import pprint
N,M,K,X = map(int,input().split())
#최단거리를 구할 리스트
# distance = [[0]*(N+1) for _ in range(N+1)]
#인접 리스트 만들기
arr = [[] for _ in range(N+1)]
for _ in range(M):
    tmp = list(map(int,input().split()))
    arr[tmp[0]].append(tmp[1])


def find_city(x,k,pre_arr) :
    global res
    if k == K :
        if x != X:
            res.append(x)
        return
    else :
        for i in arr[x] :
            if i not in pre_arr :
                find_city(i,k+1,arr[x])

res = []
for value in arr[X]:
    find_city(value,1,arr[X])

if res :
    for r in res :
        print(r)
else :
    print(-1)

# 반복문 이용
N,M = map(int,input().split())

cards = list(map(int,input().split()))
min_gap = int(1e9)
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res = cards[i]+cards[j]+cards[k]
            now_gap = M-res
            if min_gap > now_gap and now_gap>=0 :
                min_gap = now_gap
                ans = res
print(ans)

# itertools 이용
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

combis = list(map(sum, combinations(cards, 3)))
min_gap = int(1e9)
for combi in combis:
    now_gap = M - combi
    if now_gap < min_gap and now_gap>=0:
        min_gap = now_gap
        res = combi
print(res)

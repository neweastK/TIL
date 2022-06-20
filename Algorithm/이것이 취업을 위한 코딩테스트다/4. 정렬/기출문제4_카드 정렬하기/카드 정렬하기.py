import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    heapq.heappush(heap,int(sys.stdin.readline()))
res = 0
while len(heap)>1 :
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    heapq.heappush(heap,A+B)
    res+=(A+B)

print(res)
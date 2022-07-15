import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(arr,x)
    else :
        res = heapq.heappop(arr) if arr else 0
        print(res)

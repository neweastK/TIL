import sys
import math
input = sys.stdin.readline

def count_child(base):
    cnt = 0
    for c in colors:
        cnt += math.ceil(c/base)
    return cnt

N,M = map(int,input().split())
colors = [ int(input()) for _ in range(M)]

start = 1
end = max(colors)
answer = 0
while start<=end:
    mid = (start+end)//2
    res = count_child(mid)
    if res<=N:
        end = mid-1
        answer = mid
    else:
        start = mid+1
print(answer)
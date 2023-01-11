import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
arr = list(map(int,input().split()))
res = [0]

for i in range(N):
    if res[-1]<arr[i]:
        res.append(arr[i])
    else:
        idx = bisect_left(res,arr[i])
        res[idx] = arr[i]

print(len(res)-1)
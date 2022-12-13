import sys
input = sys.stdin.readline

from collections import Counter

def search_num(target):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return False


N = int(input())
counts = Counter(map(int,input().split()))
arr = list(counts.keys())
arr.sort()


M = int(input())
checks = list(map(int,input().split()))
res = []
for check in checks:
    if search_num(check):
        res.append(counts[check])
    else:
        res.append(0)
print(*res)
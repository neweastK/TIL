import sys
input = sys.stdin.readline

def count_out(k):
    own = k
    cnt = 0
    for day in days:
        if day > own:
            own = k
            cnt+=1
        own -= day
    return cnt

N, M = map(int,input().split())
days = [int(input()) for _ in range(N)]
start = max(days)
end = sum(days)

while start<=end:
    mid = (start+end)//2
    if count_out(mid)>=M:
        start = mid+1
    else:
        end = mid-1
        answer = mid
print(answer)
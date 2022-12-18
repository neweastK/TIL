import sys
input = sys.stdin.readline

def check_able(base_time):
    cnt = 0
    for task in tasks:
        cnt+=base_time//task

    return cnt

N,M = map(int,input().split())
tasks = [ int(input()) for _ in range(N)]

start = 1
end = (10**9)*1000000000

while start<=end:
    mid = (start+end)//2
    total = check_able(mid)
    if total>=M:
        end = mid-1
        answer = mid
    else:
        start = mid+1

print(answer)

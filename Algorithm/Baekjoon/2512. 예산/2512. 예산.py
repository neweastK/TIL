import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int,input().split()))
maximum = int(input())

if sum(requests)<=maximum:
    answer = max(requests)
else:
    start = 0
    end = max(requests)
    answer = 0
    while start<=end:
        mid = (start+end)//2
        total = 0
        for i in range(N):
            if requests[i]>=mid:
                total+=mid
            else:
                total+=requests[i]

        if total>maximum:
            end = mid-1
        else:
            start = mid+1
            answer = mid
print(answer)
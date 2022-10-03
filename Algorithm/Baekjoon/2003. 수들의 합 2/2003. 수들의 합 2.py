import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0
for i in range(N):
    start = arr[i]

    if start == M :
        cnt+=1
        continue
    tmp = start
    for j in range(i+1,N):
        tmp += arr[j]
        if tmp>M :
            break
        elif tmp == M :
            cnt += 1
            break
print(cnt)
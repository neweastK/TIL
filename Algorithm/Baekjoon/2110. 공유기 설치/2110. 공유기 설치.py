import sys
input = sys.stdin.readline

N,C = map(int,input().split())

houses = [ int(input()) for _ in range(N)]
houses.sort()
start = 1
end = houses[-1]-houses[0]

while start<=end:
    # 공유기 간의 최소 거리 (이 길이보다는 길거나 같아야 공유기 설치 가능!)
    mid = (start+end)//2
    cnt = 1
    base = houses[0]
    for i in range(1,N):
        if houses[i]-base >= mid:
            cnt+=1
            base = houses[i]

    if cnt>=C:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)
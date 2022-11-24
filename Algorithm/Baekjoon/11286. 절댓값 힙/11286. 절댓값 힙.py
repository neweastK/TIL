import sys
import heapq
input = sys.stdin.readline

arr1 = []
arr2 = []

N = int(input())
for _ in range(N):
    tmp = int(input())
    if tmp>0:
        heapq.heappush(arr1,tmp)
    elif tmp<0:
        heapq.heappush(arr2,-tmp)
    else:
        a = heapq.heappop(arr1) if len(arr1) else 0
        b = heapq.heappop(arr2) if len(arr2) else 0
        # 절댓값 크기 비교
        if a and b:
            if a>=b:
                heapq.heappush(arr1,a)
                print(-b)
            else:
                heapq.heappush(arr2,b)
                print(a)
        else:
            if a == 0:
                print(-b)
            else:
                print(a)
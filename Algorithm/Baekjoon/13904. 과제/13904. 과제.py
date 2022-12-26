import sys
import heapq
input = sys.stdin.readline

N = int(input())
homeworks = []
days_cnt = 0
for _ in range(N):
    homework = list(map(int,input().split()))
    homeworks.append((-homework[1],homework[0]))
    if homework[0] > days_cnt:
        days_cnt = homework[0]

days = [0]*days_cnt
heapq.heapify(homeworks)
total = 0
for _ in range(N):
    score,day = heapq.heappop(homeworks)
    if days[day-1] == 0:
        total += (-score)
        days[day-1] = 1
    else:
        for i in range(day-2,-1,-1):
            if days[i] == 0:
                days[i] = 1
                total += (-score)
                break
print(total)

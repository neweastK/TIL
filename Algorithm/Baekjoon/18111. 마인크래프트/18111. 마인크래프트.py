import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]

numbers = []
for i in range(N):
    tmp = list(set(maps[i]))
    numbers.extend(tmp)
limit = max(set(numbers))
# 배열에 속한 숫자들
res = []

# 모든 배열의 수를 numbers를 돌면서 각 숫자로 맞춰보자
for number in range(0,limit+1):
    imsi_B = B
    time = 0
    for i in range(N):
        for j in range(M):
            tmp = number - maps[i][j]
            # number에 맞추기 위해 tmp만큼 더해줘야함
            if tmp<0 :
                time += abs(tmp)*2
                imsi_B += abs(tmp)
            elif tmp>0 :
                time += tmp
                imsi_B -= tmp
    if imsi_B<0:
        continue
    else :
        res.append([time,number])

res.sort(key=lambda x:(x[0],-x[1]))
print(*res[0])
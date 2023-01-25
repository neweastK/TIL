N = int(input())
lectures = [list(map(int,input().split())) for _ in range(N)]

res = 0
lectures.sort(key=lambda x:(x[1],x[0]))
tmp = 0
for lecture in lectures:
    start,end = lecture
    if tmp<=start:
        tmp = end
        res += 1

print(res)
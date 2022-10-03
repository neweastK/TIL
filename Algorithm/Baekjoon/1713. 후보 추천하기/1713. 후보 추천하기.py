N = int(input())
C = int(input())
arr = list(map(int,input().split()))

frame = [[0,0,0] for _ in range(N)]

time = 1
for a in arr:
    frame.sort(key=lambda x:(-x[1],-x[2]))
    # 이미 있는지 확인
    if a in list(map(lambda x:x[0],frame)):
        frame[list(map(lambda x:x[0],frame)).index(a)][1] += 1
        continue
    # 없다면
    else :
        last = frame.pop()
        frame.append([a,0,time])
        time+=1
res = sorted(list(map(lambda x:x[0],frame)))
for r in res :
    if r != 0 :
        print(r)
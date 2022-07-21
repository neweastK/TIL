N = int(input())

members = [ list(map(int,input().split())) for _ in range(N)]

for i in range(len(members)):
    now = members[i]
    cnt = 0
    for j in range(len(members)):
        if j == i :
            continue
        else :
            # 나보다 큰 사람의 수
            if now[0] < members[j][0] and now[1] < members[j][1] :
                cnt+=1
    print(cnt+1, end=' ')

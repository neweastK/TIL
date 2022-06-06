def hansoo(N):
    global cnt
    gap = []
    if len(N) == 1:
        cnt+=1
        return

    for i in range(1,len(N)) :
        # tmp는 등차
        tmp = int(N[i])-int(N[i-1])
        gap.append(tmp)
    if len(set(gap)) == 1:
        cnt+=1

T = int(input())
cnt = 0
for t in range(1,T+1):
    hansoo(str(t))

print(cnt)
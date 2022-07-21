N = int(input())

ans = []
for i in range(1,1000001) :
    if i > N :
        break
    else :
        res = i
        tmp = str(i)
        for s in tmp :
            res += int(s)
        if res == N :
            ans.append(i)
if ans :
    print(min(ans))
else :
    print(0)

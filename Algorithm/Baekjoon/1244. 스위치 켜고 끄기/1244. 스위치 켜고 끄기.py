def boy(num):
    global switch
    for i in range(num,N+1) :
        if i % num == 0 :
            switch[i] = abs(switch[i]-1)
    return

def girl(num):
    global switch
    k=1
    switch[num] = abs(switch[num] - 1)
    while num-k>0 and num+k<N+1 :
        if switch[num+k] == switch[num-k] :
            switch[num+k] = abs(switch[num+k] - 1)
            switch[num-k] = abs(switch[num-k] - 1)
            k+=1
        else :
            break
    return

N = int(input())
switch = [0]+list(map(int,input().split()))
S = int(input())
for _ in range(S) :
    x, num = map(int,input().split())
    if x == 1 :
        boy(num)
    else :
        girl(num)

res = switch[1:]
for l in range(0,len(res),20):
    print(*res[l:l+20], end="")
    print()

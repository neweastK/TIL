import sys
sys.stdin = open("input.txt")

def in_order(v,chd):
    global lst
    if chd[v]:
        in_order(chd[v][0],chd)
        print(lst[v],end="")
        if len(chd[v]) > 1 :
            in_order(chd[v][1],chd)
    else :
        print(lst[v],end="")

for tc in range(10):
    N=int(input())
    lst = [0]*(N+1)
    chd = [0]*(N+1)

    for i in range(1,N+1):
        tmp = input().split()
        chd[i] = list(map(int,tmp[2:]))
        lst[i] = tmp[1]

    print(f"#{tc+1} ", end="")
    in_order(1,chd)
    print()

import sys
sys.stdin = open("input.txt")

def cnt_chd(N, lst):
    global visited

    visited.append(N)

    if len(lst[N]) == 0:
        return

    else:
        cnt_chd(lst[N][0], lst)
        if len(lst[N]) > 1 :
            cnt_chd(lst[N][1], lst)


T = int(input())
for tc in range(T) :
    E, N = map(int,input().split())
    chd = [[] for i in range(E+2)]
    visited=[]
    nodes = list(map(int,input().split()))
    for i in range(0,len(nodes),2):
        chd[nodes[i]].append(nodes[i+1])
    cnt_chd(N, chd)
    print(f'#{tc+1} {len(visited)}')

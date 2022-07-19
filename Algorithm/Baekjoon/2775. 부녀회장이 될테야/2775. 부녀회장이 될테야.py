import sys

def apartment(k,n):
    global info
    # 0층의 정보
    tmp = []
    for i in range(1,n+1):
        tmp.append(sum(info[k-1][:i]))
    info.append(tmp)


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    info = [[x for x in range(1,n+1)]]

    for j in range(1,k+1):
        apartment(j,n)
    print(info[-1][-1])
# 1차로 모든 체스판의 경우의 수를 만들었음
def DFS(n,res,N) :
    global cnt
    # 조건1. 같은 열에 퀸이 있을 수 없다.
    columns = list(map(lambda x : x[1], res))
    if len(set(columns)) < n:
        return

    # 조건2. 대각선에 퀸이 있어서는 안된다.
    if len(res) > 1:
        tmp = len(res)
        for j in range(tmp - 1):
            if abs(res[-1][0] - res[j][0]) == abs(res[-1][1] - res[j][1]):  # 열의 거리 , 행의 거리 :
                return

    # 모든 조건을 충족하고 모든 퀸을 놓았다면
    if n == N :
        cnt+=1

    for i in range(N):
        # res.append((n,i))
        DFS(n+1,res+[(n,i)],N)
        # res.pop()


T=int(input())
for tc in range(T):
    N=int(input())
    cnt=0
    DFS(0,[],N)
    print(f'#{tc+1} {cnt}')

    tmp = [[x, BC[x][3]] for x in loc_a]
    tmp.sort(key=lambda x: x[1])
    print(tmp)
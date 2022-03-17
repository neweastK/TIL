import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N,M,L = map(int,input().split())
    tree = [0]*(N+1)

    for _ in range(M): # 리프 노드 값들을 모두 넣어준다
        idx,value = map(int,input().split())
        tree[idx] = value

    # 자식 노드의 위치는 k*2, k*2+1
    for i in range(N,0,-1): # 역순으로 돌아야 제대로 된 값이 나옴(자식 노드부터 채워줘야 하기 때문)
        if tree[i] : # 이미 값이 있으면 패스
            continue
        else : # 자식 노드가 한개 있는 경우, 두개 있는 경우 분리
            if i*2 < N : 
                tree[i] = tree[i*2]+tree[i*2+1]
            else : # 한개인 경우 해당값을 부모 노드에 넣어준다
                tree[i] = tree[i * 2]

    print(f'#{tc+1} {tree[L]}')


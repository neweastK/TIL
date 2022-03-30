import sys
sys.stdin = open("input.txt")

TC = int(input())

for tc in range(TC) :
    N,M = map(int,input().split())
    # W는 컨테이너 무개, T는 적재 한도
    W = list(map(int,input().split()))
    T = list(map(int,input().split()))

    W.sort() # 오름차순 정렬
    T.sort() # 내림차순 정렬

    ans=0
    while W and T :
        w = W[-1] # 가장 높은 수 꺼내기
        t = T[-1] # 가장 높은 수 꺼내기
        if t >= w : # 적재한도가 더 크다면 옮길 수 있다!
            ans+=w # 해당 무게만큼 옮기기
            W.pop() # 가장 무거운 것을 옮겼으니 제외
            T.pop() # 트럭도 이동했으니 제외
        else : # 무게가 더 높다 = 이 컨테이너는 어차피 못 옮긴다 = 포기
            W.pop() # 버린다.

    print(f'#{tc + 1} {ans}')
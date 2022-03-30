import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())

    times = [list(map(int,input().split())) for _ in range(N)]
    times.sort(key=lambda x:x[1]) #작업 완료시간을 기준으로 정렬
    res=0
    while times : #앞에서부터 하나씩 꺼내보면서 반복할 예정
        tmp = times.pop(0) #가장 앞에 아이를 꺼내줌
        cnt = 1 #꺼내준 아이부터 세기 위한 개수 cnt
        for time in times : #나머지 아이들 순회
            if time[0] < tmp[1] : #시작점이 앞에꺼 끝나는 것보다 빠르면 탈락
                continue
            else : #그게 아니라면 즉, 완료 시간이 작업 시작시간보다 빠르거나 같다면
                cnt+=1 #개수 추가
                tmp = time[:] #기준점을 변경해주어야함
        if res < cnt :
            res = cnt

    print(f"#{tc+1} {res}")
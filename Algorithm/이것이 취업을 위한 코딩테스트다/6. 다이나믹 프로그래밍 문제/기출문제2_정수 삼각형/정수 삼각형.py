N = int(input())

arr = [ list(map(int,input().split())) for _ in range(N)]

# 전체 줄 순회
for x in range(1,N):
    # 해당 줄에서 각 숫자 순회
    # 각각의 줄의 길이가 다르기 때문에 각 줄의 길이로 범위 지정
    for y in range(len(arr[x])) :
        # 만약 맨 앞의 숫자인 경우
        if y==0 :
            arr[x][y] += arr[x-1][y]
        # 맨 뒤의 숫자인 경우
        elif y==len(arr[x])-1 :
            arr[x][y] += arr[x-1][y-1]
        # 중간인 경우 == 숫자를 비교해봐야되는 경우
        else :
            tmp1 = arr[x-1][y-1]+arr[x][y]
            tmp2 = arr[x][y]+arr[x-1][y]
            arr[x][y]= tmp1 if tmp1>tmp2 else tmp2

# 마지막 줄에서 가장 큰 수를 구한다
print(max(arr[-1]))
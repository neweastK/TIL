import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
# 오큰수를 담을 배열
ans = [-1]*N
# 오른쪽 숫자부터 시작하기
for i in range(N-2,-1,-1):
    # 만약 바로 오른쪽의 수가 더 크면 해당 숫자가 가장 가까우므로 오큰수가 됨
    if arr[i] < arr[i+1] :
        ans[i] = arr[i+1]
    # 작다면?
    else :
        # 바로 오른쪽의 숫자부터 끝까지 오큰수 비교
        for j in range(i+1,N):
            # 만약 오큰수가 -1이면 오큰수는 -1
            if ans[j] == -1 :
                ans[i] = -1
                break
            # 본인보다 더 큰 오큰수를 만나면
            elif arr[i] < ans[j] :
                # 본인의 오큰수는 그 오큰수가 됨
                ans[i] = ans[j]
                break
        # 끝까지 가도 없다면, 오큰수는 -1
        else:
            ans[i] = -1

print(*ans)
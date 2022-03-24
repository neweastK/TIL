def DFS(ans, n, N, V, lst):
    global res  # 조건을 만족할 경우 결과값을 담아줄 리스트
    if ans == V:  # 만약 문제에서 제시한 값을 찾았다면
        res = lst  # 특정 자리수를 더할 때 마다 해당 자리수 번호를 추가했던 리스트를 넘겨준다
    elif n == N:
        pass
    else:
        DFS(ans + 2 ** (-n), n + 1, N, V, lst + [n])  # 한자리 아래수를 더해주는 경우, lst에 더한 자리수를 넣어줌
        DFS(ans, n + 1, N, V, lst)  # 한자리 아래수를 더하지 않는 경우


T = int(input())

for tc in range(T):

    N = 13  # 13자리가 되면 돌아오도록 설정
    V = float(input())  # 목표값
    lst = []
    res = []
    DFS(0, 1, N, V, lst)

    if res:
        # res에는 더해준 자리수들이 들어있으므로 추가적인 작업 필요 ex)[1,3] 2^-1과 2^-3값이 1이라는 뜻
        ans = [0] * res[-1]  # 결과값의 길이만큼 0으로 차있는 리스트 생성
        for i in res:  # res 값이 있다는 것은 해당 위치는 1이라는 뜻
            ans[i - 1] = 1
        ans = "".join(map(str, ans))
        print(f"#{tc + 1} {ans}")

    # res 길이가 0 이면 overflow 출력
    else:
        print(f"#{tc + 1} overflow")


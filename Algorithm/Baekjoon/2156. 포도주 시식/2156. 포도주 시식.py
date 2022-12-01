N = int(input())
wines = [int(input()) for _ in range(N)]

if N == 1:
    print(wines[0])
else:
    # 앞에꺼 안마셔
    dp1 = [0] * N
    # 앞에꺼 마셔
    dp2 = [0] * N
    dp1[0], dp2[0] = wines[0], wines[0]
    dp1[1], dp2[1] = wines[1], wines[0] + wines[1]
    for i in range(2, len(wines)):
        dp1[i] = max(max(dp1[0:i - 1]), max(dp2[0:i - 1])) + wines[i]
        dp2[i] = dp1[i - 1] + wines[i]

    res = max(max(dp1), max(dp2))
    print(res)
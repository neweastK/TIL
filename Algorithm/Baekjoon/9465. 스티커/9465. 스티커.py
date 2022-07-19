import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    first = list(map(int,input().split()))
    second = list(map(int,input().split()))

    dp = [[0]*2 for _ in range(N)]
    dp[0][0] = first[0]
    dp[0][1] = second[0]

    try:

        dp[1][0] = dp[0][1] + first[1]
        dp[1][1] = dp[0][0] + second[1]

        for i in range(2,N) :
            dp[i][0] = max(dp[i-1][1],dp[i-2][1]) + first[i]
            dp[i][1] = max(dp[i-1][0],dp[i-2][0]) + second[i]

        print(max(dp[-1]))
    except IndexError :
        print(max(dp[0]))